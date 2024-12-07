import React from "react";
import "./index.css";
import SignUp from "./components/SignUp";
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Register from "./components/Register";

function App() {
  return (
    <>
    <div className="App">
        <SignUp/>
    </div>
    <BrowserRouter>
    <Routes>
      <Route path="registr" element={<Register/>}/>
      <Route path="signup" element={<SignUp/>}/>
    </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
