FROM loopbackkr/pytorch:1.11.0-cuda11.3-cudnn8
COPY requirements.txt /root/workspace
RUN pip install -r requirements.txt

WORKDIR /root/workspace

# ENTRYPOINT "python" "-m" "evaluation"
