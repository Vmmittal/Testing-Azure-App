from flask import Flask,jsonify,request


app=Flask(__name__)




my_cars=[
  {
    "id":1,
    "model":2022,
    "Brand":"Maruti Suzuki"
  },
  {
    "id":2,
    "model":2019,
    "Brand":"Toyota"
  }
]

@app.route("/")
def func():
  return jsonify("Hello World !")




@app.route("/add-cars", methods=["POST"])
def add_cars():
   if not request.json:
    return jsonify({
      "message": "Error"
    },400)

   new_car={
    # "id":my_cars[-1]["id"] + 1,
    "model":request.json["model"],
    "Brand":request.json['Brand'],
    # "description":request.json["description"]
   } 
   my_cars.append(new_car)  
   return jsonify({
     "status":"Successfull"
   })


@app.route("/get-cars")
def get_all_cars():
  return jsonify({"data": my_cars})


if __name__ =='__main__':
 app.run(debug=True)