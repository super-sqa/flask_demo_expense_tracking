
IMAGE_NAME_OR_ID=expense

CONTAINER_NAME=expense_tracking_app

docker run --name ${CONTAINER_NAME} -p 8585:8889 -d ${IMAGE_NAME_OR_ID} 
#docker run --name expense_tracking_app -p 8585:8889 --expose 8889 expense
#docker run --name expense_tracking_app -p 5001:5001 expense
