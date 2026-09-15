import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        medical: {
          navy: "#0A192F",
          darkBlue: "#0F294A",
          blue: "#1E3A8A",
          sky: "#0284C7",
          lightSky: "#E0F2FE",
          softBlue: "#F0F7FF",
          green: "#059669",
          emerald: "#10B981",
          lightGreen: "#ECFDF5",
          danger: "#DC2626",
          dangerLight: "#FEF2F2",
        },
      },
      boxShadow: {
        glass: "0 8px 32px 0 rgba(14, 30, 64, 0.08)",
        "glass-lg": "0 16px 48px 0 rgba(14, 30, 64, 0.12)",
        glow: "0 0 40px -10px rgba(2, 132, 199, 0.3)",
        "glow-danger": "0 0 35px -5px rgba(220, 38, 38, 0.35)",
      },
    },
  },
  plugins: [],
};

export default config;
