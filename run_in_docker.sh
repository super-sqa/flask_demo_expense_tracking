
IMAGE_NAME_OR_ID=expense
CONTAINER_NAME=expense_tracking_app

HOST_PORT=8585
PATH_ON_HOST=/Users/akinfu/misc/other_projects/flask_demo_expense_tracking/app

docker run --name ${CONTAINER_NAME} \
-v ${PATH_ON_HOST}:/my_flask_app/app \
-p ${HOST_PORT}:8889 \
-d \
${IMAGE_NAME_OR_ID}

