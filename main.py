import gradio as gr
from pathlib import Path
import os
import datetime

current_file_path = Path(__file__).resolve()
absolute_path = "C:\\Users"

def get_file_content(file):
    # 파일 메타정보 가져오기
    if file and os.path.exists(file):
        file_stat = os.stat(file)
        file_info = {
            '파일 경로': file,
            '파일 크기': f'{file_stat.st_size} 바이트',
            '생성 시간': datetime.datetime.fromtimestamp(file_stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
            '최종 수정 시간': datetime.datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
            '최종 접근 시간': datetime.datetime.fromtimestamp(file_stat.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
        }
        return '\n'.join([f'{k}: {v}' for k, v in file_info.items()])
    return file

with gr.Blocks() as demo:
    with gr.Row():
        file = gr.FileExplorer(
            root_dir=absolute_path,
            ignore_glob="**/*.exe",
            file_count="single",
        )
        with gr.Column():
            code = gr.Code(language="python")
            btn = gr.Button("파일 열기")
            
    file.change(get_file_content, file, code)
    btn.click(lambda file: os.startfile(file), file, None)
    

if __name__ == "__main__":
    demo.launch()
