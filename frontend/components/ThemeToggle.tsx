"use client";

import { useTheme } from "@/providers/ThemeProvider";
import { MoonIcon, SunIcon, SystemIcon } from "./Icons";

export default function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  return (
    <div className="more-options-theme">
      <button
        className={`btn-theme ${theme === "light" ? "active" : ""}`}
        onClick={() => setTheme("light")}
      >
        <SunIcon styles="theme-icon" />
      </button>

      <button
        className={`btn-theme ${theme === "dark" ? "active" : ""}`}
        onClick={() => setTheme("dark")}
      >
        <MoonIcon styles="theme-icon" />
      </button>

      <button
        className={`btn-theme ${theme === "system" ? "active" : ""}`}
        onClick={() => setTheme("system")}
      >
        <SystemIcon styles="theme-icon" />
      </button>
    </div>
  );
}
