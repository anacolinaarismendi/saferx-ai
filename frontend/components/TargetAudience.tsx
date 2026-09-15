"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { UserCheck, Stethoscope, Siren, Building2, CheckCircle2 } from "lucide-react";

export const TargetAudience: React.FC = () => {
  const { t } = useLanguage();

  const audiences = [
    {
      icon: <Stethoscope className="w-8 h-8 text-sky-400" />,
      title: t.target.primaryCare.title,
      role: t.target.primaryCare.role,
      desc: t.target.primaryCare.desc,
      feature: t.target.primaryCare.feature,
    },
    {
      icon: <Siren className="w-8 h-8 text-sky-400" />,
      title: t.target.emergency.title,
      role: t.target.emergency.role,
      desc: t.target.emergency.desc,
      feature: t.target.emergency.feature,
    },
    {
      icon: <Building2 className="w-8 h-8 text-sky-400" />,
      title: t.target.directors.title,
      role: t.target.directors.role,
      desc: t.target.directors.desc,
      feature: t.target.directors.feature,
    },
  ];

  return (
    <section id="clientes" className="py-24 bg-medical-navy text-white relative overflow-hidden">
      {/* Background radial glow */}
      <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-sky-600/10 blur-[140px] rounded-full pointer-events-none" />
      <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-blue-900/30 blur-[120px] rounded-full pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-white/10 border border-white/15 text-sky-300 text-xs font-bold uppercase tracking-wider mb-4 backdrop-blur-sm">
            <UserCheck className="w-3.5 h-3.5" />
            <span>{t.target.tag}</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
            {t.target.title}
          </h2>
          <p className="mt-4 text-base sm:text-lg text-slate-300">
            {t.target.subtitle}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {audiences.map((card, idx) => (
            <div
              key={idx}
              className="rounded-3xl p-8 bg-white/[0.04] backdrop-blur-md border border-white/10 hover:border-sky-400/40 hover:bg-white/[0.07] transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1 shadow-2xl"
            >
              <div>
                <div className="w-16 h-16 rounded-2xl bg-white/10 flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                  {card.icon}
                </div>
                <span className="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">
                  {card.role}
                </span>
                <h3 className="text-2xl font-bold text-white mb-3">
                  {card.title}
                </h3>
                <p className="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
                  {card.desc}
                </p>
              </div>

              <div className="pt-5 border-t border-white/10 flex items-center gap-2 text-xs text-emerald-300 font-semibold">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                <span>{card.feature}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
