import type { Metadata } from "next";
import "./globals.css";
import { LanguageProvider } from "@/context/LanguageContext";

export const metadata: Metadata = {
  title: "SafeRx AI | Seguridad Farmacológica Instantánea en tu Consulta",
  description:
    "Reduce errores médicos y ahorra tiempo con alertas de interacción basadas en evidencia oficial, integradas a tu historial clínico EHR.",
  keywords: [
    "HealthTech",
    "Seguridad Farmacológica",
    "Interacciones Medicamentosas",
    "EHR",
    "Polifarmacia",
    "IA Médica",
  ],
  authors: [{ name: "SafeRx AI Team" }],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" className="scroll-smooth">
      <body className="antialiased font-sans bg-[#f8fafc] text-slate-900 selection:bg-blue-900 selection:text-white">
        <LanguageProvider>{children}</LanguageProvider>
      </body>
    </html>
  );
}
