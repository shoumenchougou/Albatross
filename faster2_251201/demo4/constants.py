from pathlib import Path


DEFAULT_MODEL_DIR = str(Path(__file__).resolve().parent.parent)
DEFAULT_MODEL_NAME = "/mnt/sda1/rwkv_weights/rwkv7-g1f-7.2b-20260414-ctx8192"
DEFAULT_PROMPT = "User: 编程网页，创建一个温馨的本地咖啡馆官网，采用暖色调配色方案，包括浅米色、奶油白和柔和的木质色系，搭配优雅的排版风格，使用衬线字体和适度的间距。首页包含品牌介绍、菜单展示、活动信息和联系方式等模块，页面内容简洁明了，突出咖啡馆的特色和氛围\n\nAssistant: <think"
TITLE_MODEL_NAME = "RWKV-7 7.2B"
TITLE_PRECISION = "FP16"
TITLE_GPU_NAME = "RTX 5090"
WINDOW_TITLE = "RWKV-7 batch demo4"
