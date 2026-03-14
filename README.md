
Simple MLOps Project

Steps:

1. Train model
python train.py

2. Run UI
streamlit run app.py

3. Docker build
docker build -t student-pass-ml .

4. Docker run
docker run -p 8501:8501 student-pass-ml
