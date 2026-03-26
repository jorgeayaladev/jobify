"use client"

import { useForm, FormProvider } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { EmailIcon, LockIcon } from "../Icons";

import {
  LoginSchema,
  defaultValues,
  type LoginSchemaType,
} from "@/schemas/LoginSchema";

export default function LoginForm() {
  const methods = useForm<LoginSchemaType>({
    resolver: zodResolver(LoginSchema),
    defaultValues: defaultValues,
  });

  const {
    handleSubmit,
    register,
    formState: { errors },
  } = methods;

  const onSubmit = (data: LoginSchemaType) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log("Form submitted", data);
        resolve(true);
      }, 1000);
    });
  };

  return (
    <FormProvider {...methods}>
      <form onSubmit={handleSubmit(onSubmit)} className="login-form">
        <div className="form-group">
          <label htmlFor="login_email" className="form-label">
            <EmailIcon /> Correo electrónico
          </label>
          <div className="input-group">
            <EmailIcon />
            <input
              id="login_email"
              type="email"
              placeholder="chef@turestaurante.com"
              {...register("email")}
              required
            />
            {errors.email && <span>{errors.email.message}</span>}
          </div>
        </div>

        <div className="form-group">
          <label className="form-label">
            <LockIcon /> Contraseña
          </label>
          <div className="input-group">
            <LockIcon />
            <input type="password" placeholder="••••••••" required />
            <i className="fas fa-eye password-toggle"></i>
          </div>
        </div>

        <div className="form-options">
          <label className="remember-me">
            <input type="checkbox" defaultChecked />
            <span>Mantener sesión</span>
          </label>
          <a href="#" className="forgot-link">
            ¿Olvidaste tu contraseña?
          </a>
        </div>

        <button type="submit" className="btn-login">
          <i className="fas fa-sign-in-alt"></i>
          Acceder al Dashboard
        </button>
      </form>
    </FormProvider>
  );
}
