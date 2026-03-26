import React from "react";
import { EyeCloseIcon, EyeIcon } from "../Icons";

type Props = {};

export default function EyeToggle({}: Props) {
  return (
    <button
      className={`btn-theme`}
      onClick={() => {}}
    >
      <EyeIcon/>
      <EyeCloseIcon/>
    </button>
  );
}
