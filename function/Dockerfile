FROM public.ecr.aws/lambda/python:3.8

RUN yum -y update && \
    yum -y install yum-utils && \
    yum-config-manager --add-repo https://download.opensuse.org/repositories/home:/Alexander_Pozdnyakov/RHEL_7/ && \
    rpm --import https://build.opensuse.org/projects/home:Alexander_Pozdnyakov/public_key && \
    yum -y install tesseract tesseract-langpack-jpn

COPY app.py requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
