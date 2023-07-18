import React, { useState } from 'react'
// import style from './user.module.css'
import { Link } from 'react-router-dom'
import axios from 'axios';

const UserLogin = ()=> {
  let [phone,setPhone]=useState("");
  let[password,setPassword]=useState("");
  
  let phonedata=(e)=>{
    setPhone(e.target.value)

  }
  let passdata =(e)=>{
    setPassword(e.target.value)
  }

 
 
  let handleSubmit= (e)=>{
    console.log("data");
    e.preventDefault();
    let userlogin={phone,password}
    // console.log("payload"+AuthUser.phone);
      axios.get("http://localhost:8080/user/verify",userlogin)
      .then((rep)=>{
                console.log("then block"+rep.phone.data);
                console.log("server res");
                
    })
    .catch((e)=>{
      console.log("Sonething Wrong"+e);
    })
  }
    return (
      <div>
    <div >
     <h2>Login</h2>
     <br></br>
      <form >
        <div >
      <label htmlFor="">Phone</label>
      <input type="tel" placeholder='Enter the phone number'  value={phone} onChange={phonedata} />
          <label htmlFor="">Password</label>
      <input type="password" placeholder='********' id='password'  value={password} onChange={passdata} />
      <button onClick={handleSubmit} >Log In</button>
      
      </div>
      </form>
      <br />
      {/* <button className="link-btn" onClick={() => props.onFormSwitch('register')}>Don't have an account? Register here.</button> */}
            {/* <Link to={"/userreg"}>
                  <pre>Create a Account</pre>
            </Link> */}
         
    </div>
    </div>
  )
}

export default UserLogin;