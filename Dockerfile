FROM spark-base:0.1

RUN pip install -r requirements.txt
ENV SUBMIT_ARGS="--conf spark.driver.cores=3 --conf spark.driver.memory=2g --conf spark.executor.cores=2 --conf spark.executor.memory=2g"
ENV APP_ARGS="--file yarn-site.xml --char01 c --char02 y"

CMD [ "submit.sh" ]