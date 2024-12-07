import React from 'react'
import RegisterModal from "./RegisterModal"

export default function Register() {
  return (
    <div>
        <body>
            <div className="container">
                <div className="img">
                  <img src={`${process.env.PUBLIC_URL}/Group 18.png`} alt="Group 18" />
                </div>
                <RegisterModal/>
            </div>
        </body>
    </div>
  )
}
