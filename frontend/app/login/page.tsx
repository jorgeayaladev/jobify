import {
  EmailIcon,
  LockHeartIcon,
  LockIcon,
  LogoIcon,
  ShieldIcon,
  TermsConditionsIcon,
} from "@/components/Icons";
import "./login.css";
import Link from "next/link";
import LoginForm from "@/components/forms/LoginForm";

type Props = {};

export default function Login({}: Props) {
  return (
    <div className="login-fullscreen">
      {/*<!-- Lado izquierdo - Marca y contenido -->*/}
      <div className="brand-side">
        <div className="brand-header">
          <div className="brand-logo">
            <LogoIcon styles="logo-icon" />
            <span>
              Gurm<span>ify</span>
            </span>
          </div>

          <div className="brand-quote">
            <h1>Gestiona tu restaurante como un experto</h1>
            <p>
              La plataforma integral que transforma la administración de tu
              negocio gastronómico
            </p>

            <div className="brand-stats">
              <div className="stat-item">
                <span className="stat-number">500+</span>
                <span className="stat-label">RESTAURANTES</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">50k+</span>
                <span className="stat-label">CLIENTES DIARIOS</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">98%</span>
                <span className="stat-label">SATISFACCIÓN</span>
              </div>
            </div>
          </div>
        </div>

        <div className="brand-footer">
          <Link href={`/security`}>
            <ShieldIcon styles="brand-footer-icon" /> Seguridad
          </Link>
          <Link href={`/privacy`}>
            <LockHeartIcon styles="brand-footer-icon" /> Privacidad
          </Link>
          <Link href={`/conditions`}>
            <TermsConditionsIcon styles="brand-footer-icon" /> Términos y
            condiciones
          </Link>
        </div>
      </div>

      {/*<!-- Lado derecho - Login -->*/}
      <div className="login-side">
        <div className="login-container">
          <div className="login-header">
            <h2>Acceso Privado</h2>
            <p>
              <i className="fas fa-user-tie"></i> Personal autorizado
            </p>
          </div>

          <LoginForm/>

          {/*<!-- Mensaje de acceso restringido -->*/}
          <div className="restricted-message">
            <i className="fas fa-exclamation-triangle"></i>
            <p>
              <strong>Acceso exclusivo</strong> para personal de restaurantes
              con suscripción activa. Si eres cliente y necesitas acceso,
              contacta a tu gerente.
            </p>
          </div>

          <div className="support-link">
            <a href="#">
              <i className="fas fa-headset"></i>
              ¿Problemas para acceder? Contacta a soporte
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
