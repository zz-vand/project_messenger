import React from 'react'
import IMAGE from "./Group 18.png";
import SignUpmodal from './SignUpmodal'


export default function SignUp() {
  return (
    <div>
        <body>
            <div className="container">
                <div className="img">
                    <img src={IMAGE}/>
                </div>
                <SignUpmodal/>
            </div>
        </body>
    </div>
  )
}