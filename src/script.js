var Driver=require("selenium-webdriver")


function sleep(time){
    return new Promise(resolve => setTimeout(resolve, time));
}


x=0
async function Gmail(name,lastname,username,password,confirm,number){
	//start web browser: run "Firefox"
	const browser= new Driver
	.Builder().usingServer()
	.forBrowser("firefox").build()
    // context  the gmail sing up and url
    browser.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail&hl=tr&dsh=S-2113698525%3A1619302723782419&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
    var liste=[
    	browser.findElement(Driver.By.name("firstName")),
    	browser.findElement(Driver.By.name("lastName")),
    	browser.findElement(Driver.By.name("Username")),
    	browser.findElement(Driver.By.name("Passwd")),
    	browser.findElement(Driver.By.name("ConfirmPasswd")),
    ]
    liste[0].sendKeys(name)
	liste[1].sendKeys(lastname)
	liste[2].sendKeys(username)
	liste[3].sendKeys(password)
	liste[4].sendKeys(confirm)
    browser.findElement(Driver.By.css("button")).click()
    //part 2
    //tel number
    await sleep(100000)
    browser.findElement(Driver.By.id("phoneNumberId")).sendKeys(number)
    browser.findElement(Driver.By.css("button")).click()
    x+=1
    console.log(x)
    await sleep(100000)
    //getCode(browser,Driver,x)
    var {sms}=require("../sms-data.json")
    var str=sms[x]
    console.log(str)
    browser.findElement(Driver.By.name("code")).sendKeys(str)
    browser.findElement(Driver.By.xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]")).click()

}

//get sms verification code with file smsCode.txt
const getCode=(browser,Driver,z)=>{
    //get byname
    var {sms}=require("../sms-data.json")
    var str=sms[z]
    browser.findElement(Driver.By.name("code")).sendKeys(str)
    browser.findElement(Driver.By.xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/button/div[2]")).click()
    console.log(sms[z])
}

exports.Gmail=Gmail


