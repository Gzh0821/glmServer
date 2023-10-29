import requests
from asgiref.sync import async_to_sync
from transformers import AutoModel, AutoTokenizer

MODEL_PATH = "THUDM/"
MODEL_NAME = "chatglm2-6b-int4"
SDW_URL = "http://127.0.0.1:7860"
SD_MODEL_NAME = "AnythingV5Ink_ink.safetensors [a1535d0a42]"
TEMPLATE = '''
以下提示用于指导Al绘画模型创建图像。它们包括人物外观、背景、颜色和光影效果，以及图像的主题和风格等各种细节。这些提示的格式通常包括带权重的数字括号，用于指定某些细节的重要性或强调。例如，"(masterpiece:1.4)"表示作品的质量非常重要。以下是三个示例：
1. (8k, RAW photo, best quality, masterpiece:1.2),(realistic, photo-realistic:1.37), ultra-detailed, 1girl, cute, solo, beautiful detailed sky, detailed cafe, night, sitting, dating, (nose blush), (smile:1.1),(closed mouth), medium breasts, beautiful detailed eyes, (collared shirt:1.1), bowtie, pleated skirt, (short hair:1.2), floating hair, ((masterpiece)), ((best quality)),
2. (masterpiece, finely detailed beautiful eyes: 1.2), ultra-detailed, illustration, 1 girl, blue hair black hair, japanese clothes, cherry blossoms, tori, street full of cherry blossoms, detailed background, realistic, volumetric light, sunbeam, light rays, sky, cloud,
3. highres, highest quallity, illustration, cinematic light, ultra detailed, detailed face, (detailed eyes, best quality, hyper detailed, masterpiece, (detailed face), blue hairlwhite hair, purple eyes, highest details, luminous eyes, medium breats, black halo, white clothes, backlighting, (midriff:1.4), light rays, (high contrast), (colorful)

仿照之前的提示，使用英文，写一段描写如下要素的提示：'''

PAYLOAD_TEMPLATE = {
    "negative_prompt": "nsfw,logo,text,badhandv4,EasyNegative,ng_deepnegative_v1_75t,rev2-badprompt,"
                       "verybadimagenegative_v1.3,negative_hand-neg,mutated hands and fingers,poorly drawn face,"
                       "extra limb,missing limb,disconnected limbs,malformed hands,ugly,",
    "width": 512,
    "height": 512,
    'sampler_index': 'DPM++ SDE',
    "cfg_scale": 7,
    "override_settings": {"sd_model_checkpoint": SD_MODEL_NAME},
    "restore_faces": "false",
    "tiling": "false",
    "denoising_strength": 0.75,
}
tokenizer = AutoTokenizer.from_pretrained(f"{MODEL_PATH}{MODEL_NAME}", trust_remote_code=True)
model = AutoModel.from_pretrained(f"{MODEL_PATH}{MODEL_NAME}",
                                  trust_remote_code=True).cuda()
model = model.eval()


@async_to_sync
async def generate_text(input_text: str) -> str:
    chat_response, _ = model.chat(
        tokenizer, f"{TEMPLATE}{input_text}", history=[], temperature=0.6)
    return chat_response


@async_to_sync
async def generate_picture(prompt: str) -> str:
    payload = PAYLOAD_TEMPLATE.copy()
    payload['prompt'] = prompt
    response = requests.post(url=f'{SDW_URL}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    return r['images'][0]
