var express=require("express")
var path=require("path")
var app=express()
var gmail=require("./script")
app.use(express.static("public"))

app.get("/index.html",(req,res)=>{
	res.sendFile(path.join(__dirname+"/index.html"))


})


app.get("/api/index.json",(req,res,next)=>{
	
	//1. get values in index.html
	var number=0 
	var value_list={
		username:req.query.username,
		lastname:req.query.lastname,
		email:req.query.gmail,
		password:req.query.password,
		approve:req.query.approve,
		number:req.query.number
	}	
	console.log(value_list)

	gmail.Gmail(value_list.username,value_list.lastname,value_list.email,value_list.password,value_list.approve,value_list.number)
})

port =8080
host="localhost"
app.listen({port})
console.log("http://localhost:"+port)

