import React, { useState} from 'react'

const SignUpmodal = () => {
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [isValidPassword, setisValidPassword] = useState("");

    const checkPassword = async (loginData) => {
        try {
            const response = await fetch('', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(loginData),
            });
            const data = await response.json();
            if (data.isValid) {
                setisValidPassword(true);
            } else {
                setisValidPassword(false);
            }
        } catch (error) {
            console.error(error);
        }
    };

    const handleChange = (e) => {
        if(e.target.name === "username"){
            setUsername(e.target.value);
        } else {
            setPassword(e.target.value);
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const loginData = {
            username: username,
            password: password
        };
        checkPassword(loginData);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div className="sign_up">
                            <div className="place">
                                <h2>Войти в аккаунт</h2>
                                <div className="input1">
                                    <label className="name" for="username">Имя пользователя</label>
                                    <input
                                    type="text" placeholder="введите имя пользователя" className="username"
                                    name="username"
                                    value={username}
                                    onChange={handleChange}
                                    />
                                </div>
                                <div className="input2">
                                    <label for="password">Пароль</label>
                                    <input type="password" placeholder="введите пароль" className="password"
                                    name="password"
                                    value={password}
                                    onChange={handleChange}
                                    />
                                    <label className="pass" for="password"><a href="#">Забыли пароль?</a></label>
                                </div>
                                <button type="submit" className="btn">Войти</button>
                                <p>У вас нет аккаунта? <a href="#">Зарегистрироваться</a></p>
                            </div>
                        </div>
            </form>
        
        </div>
  )
}
export default SignUpmodal;