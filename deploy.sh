cd dist
zip -r function.zip ../lambda_function.py ../requests
cd ../
echo "==================================================================="
echo "Please choose a function to deploy to..."
echo ""
aws lambda list-functions | grep "FunctionName"
echo ""
echo "Then run the following:"
echo ""
echo "            aws lambda update-function-code --zip-file fileb://dist/function.zip --publish --function-name NAME-OF-LAMBDA-FUNCTION"
echo ""