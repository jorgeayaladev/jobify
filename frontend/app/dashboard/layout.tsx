import { Suspense } from "react";
import Loading from "./loading";
import "./layout.css";
import {
  CloseIcon,
  HamburguerIcon,
  HelpIcon,
  LogoIcon,
  LogoutIcon,
  SettingsIcon,
  SidebarIcon,
  UserIcon,
} from "@/components/Icons";
import Link from "next/link";
import Image from "next/image";
import ThemeToggle from "@/components/ThemeToggle";
import NavMenu from "@/components/sidebar/NavMenu";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div>
      {/*<!-- Sidebar toggle -->*/}
      <input type="checkbox" id="sidebar-toggle" className="sidebar-toggle" />

      {/*<!-- Sidebar -->*/}
      <aside className="sidebar">
        <div className="navbar">
          <div className="logo">
            <LogoIcon styles="logo-icon" />
            <div className="logo-text">
              Gurm<span>ify</span>
            </div>
          </div>

          {/*<!-- Sidebar toggle icon -->*/}
          <label htmlFor="sidebar-toggle" className="sidebar-toggle-label">
            <SidebarIcon styles="sidebar-icon" />
            <HamburguerIcon styles="hamburguer-icon" />
            <CloseIcon styles="close-icon" />
          </label>
        </div>

        <div className="restaurant-info">
          <Image
            className="restaurant-logo"
            src="https://lalucha.com.pe/wp-content/uploads/2024/12/Recurso-1-1-1.png"
            width={40}
            height={40}
            alt="La Lucha"
          />
          <div className="restaurant-text">
            <h2>La Lucha</h2>
            <h3>Sanguchería Criolla</h3>
          </div>
        </div>

        <NavMenu />

        <div className="other-options">
          {/*<!-- Other options toggle -->*/}
          <input
            type="checkbox"
            id="options-toggle"
            className="options-toggle"
          />

          <div className="user-info">
            <Image
              className="user-logo"
              src="https://lalucha.com.pe/wp-content/uploads/2024/12/Rectangle-12-min-1.png"
              width={40}
              height={40}
              alt="María Cortés"
            />
            <div className="user-text">
              <h2>María Cortés</h2>
              <h3>Gerente</h3>
            </div>
          </div>

          <div className="more-options">
            <Link href={`/profile`} className="more-options-item">
              <UserIcon styles="more-options-icon" />
              Perfil
            </Link>
            <Link href={`/help`} className="more-options-item">
              <HelpIcon styles="more-options-icon" />
              Ayuda
            </Link>
            <Link href={`/logout`} className="more-options-item">
              <LogoutIcon styles="more-options-icon" />
              Cerrar sesión
            </Link>
            <ThemeToggle />
          </div>

          <label htmlFor="options-toggle" className="options-toggle-label">
            <SettingsIcon styles="settings-icon" />
          </label>
        </div>
      </aside>

      {/*<!-- Contenido principal -->*/}
      <main className="main-content">
        <Suspense fallback={<Loading />}>{children}</Suspense>
      </main>
    </div>
  );
}
