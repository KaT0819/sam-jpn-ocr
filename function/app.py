import json
import pyocr
import boto3
from PIL import Image

s3 = boto3.resource('s3')
bucket = s3.Bucket('jpn-ocr-20210521')

def lambda_handler(event, context):
    print(event)
    for record in event['Records']:
        # ファイル名を取得
        s3_key = record['s3']['object']['key']
        file_name = s3_key.split('/')[-1]
        # ファイルを /tmp へダウンロード
        bucket.download_file(s3_key, f"/tmp/{file_name}")
        # pyocrの設定
        tool = pyocr.get_available_tools()[0]
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        # 文字列の抽出
        img = Image.open(f"/tmp/{file_name}")
        text = tool.image_to_string(img, lang='jpn', builder=builder)
        # 文字列をログに出力
        print(text)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                'text': text,
            }
        ),
    }
