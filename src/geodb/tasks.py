
from celery import shared_task
from celery.utils.log import get_task_logger
from geodb.views import getLatestEarthQuake, getLatestShakemap
from geodb.EarthquakeHistoricalAnalysis import getEarthquakeHistoricalAnalysis

logger = get_task_logger(__name__)

@shared_task
def updateLatestEarthQuake():
	getLatestEarthQuake()

@shared_task
def updateLatestShakemap():
	getLatestShakemap()

@shared_task
def getEarthquakeHistorical:
	getEarthquakeHistoricalAnalysis()