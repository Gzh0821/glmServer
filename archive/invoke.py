import base64

import requests
from asgiref.sync import async_to_sync
from django.conf import settings
from transformers import AutoModel, AutoTokenizer
from diffusers import DiffusionPipeline
import torch
from io import BytesIO

TEMPLATE = """
以下提示用于指导Al绘画模型创建图像。它们包括外观和背景描述、颜色、图片质量，以及图像的主题和风格等各种细节。以下是三个示例:
第一个:"Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
第二个:"A majestic lion jumping from a big stone at night"
第三个:"sailing ship in storm by Leonardo da Vinci"
上面是三个提示的示例，仿照这些示例，使用英文，写一段描写如下要素的提示："""

PAYLOAD_TEMPLATE = {
    "negative_prompt": "nsfw,logo,text,badhandv4,EasyNegative,ng_deepnegative_v1_75t,rev2-badprompt,"
                       "verybadimagenegative_v1.3,negative_hand-neg,mutated hands and fingers,poorly drawn face,"
                       "extra limb,missing limb,disconnected limbs,malformed hands,ugly,",
    "width": 512,
    "height": 512,
    'sampler_index': 'DPM++ SDE',
    "cfg_scale": 7,
    "override_settings": {"sd_model_checkpoint": settings.SD_MODEL_NAME},
    "restore_faces": "false",
    "tiling": "false",
    "denoising_strength": 0.75,
}

tokenizer = AutoTokenizer.from_pretrained(settings.GLM_MODEL_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(settings.GLM_MODEL_PATH, trust_remote_code=True).cuda()
model = model.eval()

baseSDXL = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0",
                                         torch_dtype=torch.float16,
                                         use_safetensors=True,
                                         variant="fp16",
                                         add_watermarker=False,
                                         trust_remote_code=True).to("cuda")


@async_to_sync
async def generate_text(input_text: str) -> str:
    chat_response, _ = model.chat(
        tokenizer, f"{TEMPLATE}{input_text}", history=[], temperature=0.6)
    return chat_response


@async_to_sync
async def generate_picture(prompt: str) -> str:
    # payload = PAYLOAD_TEMPLATE.copy()
    # payload['prompt'] = prompt
    # response = requests.post(url=f'{settings.SDW_URL}/sdapi/v1/txt2img', json=payload)
    image = baseSDXL(
        prompt=prompt,
        origin_size=(512, 512),
        target_size=(512, 512),
        negative_prompt=PAYLOAD_TEMPLATE['negative_prompt'],
    ).images[0]
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str
