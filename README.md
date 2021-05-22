# 日本語OCR機能
S3への画像アップロードをトリガーにし、
画像内の日本語文字列を解読しログへ出力

SAMデプロイでコンテナ使用　ECR

### SAMデプロイ時の注意
SAMデプロイ時に指定するImage RepositoryにECRのRepository URIを指定する。

### ECR作成
aws ecr create-repository --repository-name jpn-ocr

### 画像アップロード
aws s3 cp tests/sample.png s3://jpn-ocr-20210521/sample.png
