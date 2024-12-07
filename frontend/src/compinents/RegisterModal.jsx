import React, { useState} from 'react'
import { Link } from 'react-router-dom';

const RegisterModal = () => {
    const [password, setPassword] = useState("");
    const [username, setUsername] = useState("");
    const [success, setSuccess] = useState("");

    const CreateNewAcc = async (RegisterData) => {
        try {
            const response = await fetch('', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(RegisterData),
            });
            const data = await response.json();
            if (data.isValid) {
                setSuccess(true);
            } else {
                setSuccess(false);
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
        const RegisterData = {
            username: username,
            password: password
        };
        CreateNewAcc(RegisterData);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <div className="sign_up">
                            <div className="place">
                                <h2>Регистрация</h2>
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
                                </div>
                                <button type="submit" className="btn">Зарегистрироваться</button>
                                <p>Уже есть аккаунт? <Link to="signup">Войти</Link></p>
                            </div>
                        </div>
            </form>
        </div>

  )
}
export default RegisterModal;