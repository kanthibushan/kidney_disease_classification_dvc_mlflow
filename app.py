from cnnClassifier import logger

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from cnnClassifier.pipeline.stage_02_prepare import PrepareBaseModelTrainingPipeline

from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline

from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
 
 
STAGE_NAME = "Data Ingestion stage"

try:

   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 

   data_ingestion = DataIngestionTrainingPipeline()

   data_ingestion.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

        logger.exception(e)

        raise e
 
 
 
STAGE_NAME = "Prepare base model"

try: 

   logger.info(f"*******************")

   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

   prepare_base_model = PrepareBaseModelTrainingPipeline()

   prepare_base_model.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

        logger.exception(e)

        raise e
 
 
 
STAGE_NAME = "Training"

try: 

   logger.info(f"*******************")

   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

   model_trainer = ModelTrainingPipeline()

   model_trainer.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:

        logger.exception(e)

        raise e
 
 
 
 
STAGE_NAME = "Evaluation stage"

try:

   logger.info(f"*******************")

   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

   model_evalution = EvaluationPipeline()

   model_evalution.main()

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
 
except Exception as e:

        logger.exception(e)

        raise e
 
from flask import Flask, request, jsonify, render_template

import os

from flask_cors import CORS, cross_origin

from cnnClassifier.utils.common import decodeImage

from cnnClassifier.pipeline.predict import PredictionPipeline
 
 
os.putenv('LANG', 'en_US.UTF-8')

os.putenv('LC_ALL', 'en_US.UTF-8')
 
app = Flask(__name__)

CORS(app)
 
 
class ClientApp:

    def __init__(self):

        self.filename = "inputImage.jpg"

        self.classifier = PredictionPipeline(self.filename)
 
 
@app.route("/", methods=['GET'])

@cross_origin()

def home():

    return render_template('index.html')
 
 
@app.route("/train", methods=['GET','POST'])

@cross_origin()

def trainRoute():

    os.system("python main.py")

    return "Training done successfully!"
 
 
@app.route("/predict", methods=['POST'])

@cross_origin()

def predictRoute():

    image = request.json['image']

    decodeImage(image, clApp.filename)

    result = clApp.classifier.predict()

    return jsonify(result)
 
 
if __name__ == "__main__":

    clApp = ClientApp()

    app.run(host='0.0.0.0', port=8000) #for AWS
 