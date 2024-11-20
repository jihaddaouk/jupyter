curl -X 'POST' \
  'http://0.0.0.0:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_1": 0,
  "feature_2": 0,
  "score": false
}'

curl -X 'POST' \
  'http://0.0.0.0:8000/prediction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feature_1": 0,
  "feature_2": 0,
  "score": true
}'

curl -X 'GET' \
  'http://0.0.0.0:8000/model_information' \
  -H 'accept: application/json'
