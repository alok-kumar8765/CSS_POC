import React, { useState } from 'react'
// import style from './userreg.module.css'
import axios from 'axios';

const UserReg = () => {
  let [name,setName]=useState("");
  let [email,setEmailid]=useState("");
  let [phone,setPhone]=useState("");
  let[password,setPassword]=useState("");
  let[gender,setGender]=useState("");
  let[age,setAge]=useState("")

  let namedata=(e)=>{setName(e.target.value)}
  let emaildata=(e)=>{setEmailid(e.target.value)}
  let phonedata=(e)=>{setPhone(e.target.value)}
  let passworddata=(e)=>{setPassword(e.target.value)}
  let genderdata=(e)=>{setGender(e.target.value)}
  let agedata=(e)=>{setAge(e.target.value)}

  let handleSubmit =(e)=>{
    console.log("fonr inside");
    let user={name,email,phone,password,gender,age}
    axios.post("http://localhost:8080/user",user).then((resp)=>{
      console.log("saved");
      console.log(resp.data.name);
      console.log(resp.data.email);
      console.log(resp.data.password);
      console.log(resp.data.age);
      console.log(resp.data.name);
      console.log(resp.data.name);
    })
    .catch(()=>{
      console.log("Something Went wrong");
    })
   
  }
  return (
    <div >
      <div>
        <form action="">
        <label htmlFor="">Name</label>
        <input type="text" placeholder='Enter the Name' 
        value={name} onChange={namedata}
        
        />
        <br></br>
      <label htmlFor="">Email</label>
      <input type="email" placeholder='Enter the ur email'
      value={email} onChange={emaildata}
      />
         <br></br>
      <label htmlFor="">Phone</label>
      <input type="tel" placeholder='Enter the ur phone num' 
      value={phone} onChange={phonedata}
      />
        <br></br>
        <label htmlFor="">Password</label>
        <input type="password" placeholder='********'  
        value={password} onChange={passworddata}
        />
       <div>
        <label >Gender</label>
         <label>Male</label> 
             <input 
              type="radio"  
              value={gender} onChange={genderdata} />
             <label >FeMale</label> 
             <input type="radio"
              value={gender} onChange={genderdata} />
               
       </div>
          <br></br>
               <label>Age</label>
                <input type="number" placeholder='age'
                 value={age} onChange={agedata}
                />

       </form>
       <button  onClick={handleSubmit}>SignIn</button>
  
   </div>
    </div>
  )
}

export default UserReg