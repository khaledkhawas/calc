FROM python
 
RUN pip install flask

WORKDIR /app 

EXPOSE 5000

COPY . .

CMD ["python" , "app.py" ]