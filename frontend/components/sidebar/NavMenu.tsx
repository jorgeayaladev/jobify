"use client";

import { usePathname } from "next/navigation";
import {
  BoxIcon,
  CalendarIcon,
  ChartIcon,
  ClipboardListIcon,
  DashboardIcon,
  TableIcon,
  UsersIcon,
  UtensilsIcon,
} from "../Icons";
import Link from "next/link";

export default function NavMenu() {
  const pathname = usePathname();
  const navItems = [
    {
      url: "dashboard",
      name: "dashboard",
      icon: <DashboardIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/orders",
      name: "órdenes",
      icon: <ClipboardListIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/tables",
      name: "mesas",
      icon: <TableIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/menu",
      name: "menú",
      icon: <UtensilsIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/inventory",
      name: "inventario",
      icon: <BoxIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/reservations",
      name: "reservas",
      icon: <CalendarIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/reports",
      name: "reportes",
      icon: <ChartIcon styles="nav-icon" />,
    },
    {
      url: "dashboard/clients",
      name: "clientes",
      icon: <UsersIcon styles="nav-icon" />,
    },
  ];
  return (
    <nav className="nav-menu">
      {navItems.map((el, index) => (
        <Link
          href={`/${el.url}`}
          className={`nav-item ${pathname === `/${el.url}` ? "active" : ""}`}
          key={index}
        >
          {el.icon}
          <div className="nav-text">{el.name}</div>
        </Link>
      ))}
    </nav>
  );
}
