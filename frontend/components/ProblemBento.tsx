"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { Clock, Pill, Scale, AlertTriangle, Users, TrendingUp } from "lucide-react";

export const ProblemBento: React.FC = () => {
  const { t } = useLanguage();

  return (
    <section id="problema" className="py-24 bg-white relative overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-red-50 border border-red-100 text-medical-danger text-xs font-bold uppercase tracking-wider mb-4">
            <AlertTriangle className="w-3.5 h-3.5" />
            <span>{t.problem.tag}</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-medical-navy tracking-tight leading-tight">
            {t.problem.title}
          </h2>
          <p className="mt-4 text-base sm:text-lg text-gray-600">
            {t.problem.subtitle}
          </p>
        </div>

        {/* Bento Grid Layout */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 lg:gap-8">
          {/* Bento Card 1: Falta de Tiempo (Large Span on desktop) */}
          <div className="lg:col-span-2 group relative rounded-3xl p-8 sm:p-10 bg-gradient-to-br from-blue-50/60 via-white to-gray-50 border border-blue-100/80 shadow-glass hover:shadow-glass-lg transition-all duration-300 hover:-translate-y-1">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
              <div className="w-14 h-14 rounded-2xl bg-blue-100 flex items-center justify-center text-medical-blue shadow-inner group-hover:scale-110 transition-transform">
                <Clock className="w-7 h-7" />
              </div>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full text-xs font-bold bg-blue-100/80 text-medical-blue border border-blue-200">
                <Clock className="w-3 h-3" />
                {t.problem.card1.metric}
              </span>
            </div>

            <span className="text-xs font-bold uppercase tracking-wider text-sky-600 mb-2 block">
              {t.problem.card1.tag}
            </span>
            <h3 className="text-2xl font-bold text-medical-navy mb-4">
              {t.problem.card1.title}
            </h3>
            <p className="text-gray-600 leading-relaxed text-base sm:text-lg max-w-2xl">
              {t.problem.card1.desc}
            </p>

            {/* Visual simulation inside card */}
            <div className="mt-8 pt-6 border-t border-gray-200/70 flex flex-wrap items-center gap-3 text-xs text-gray-500 font-mono">
              <span className="bg-white px-3 py-1.5 rounded-lg border border-gray-200 shadow-sm flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-amber-500" />
                Fármaco A + B (Riesgo Moderado)
              </span>
              <span className="bg-white px-3 py-1.5 rounded-lg border border-gray-200 shadow-sm flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-red-500 animate-ping" />
                Fármaco C + D (Contraindicación Crítica)
              </span>
              <span className="text-gray-400 font-sans">
                → Sin tiempo para consultar vademécum
              </span>
            </div>
          </div>

          {/* Bento Card 2: Polifarmacia */}
          <div className="group relative rounded-3xl p-8 sm:p-10 bg-gradient-to-br from-amber-50/50 via-white to-gray-50 border border-amber-100/80 shadow-glass hover:shadow-glass-lg transition-all duration-300 hover:-translate-y-1">
            <div className="flex items-center justify-between mb-6">
              <div className="w-14 h-14 rounded-2xl bg-amber-100 flex items-center justify-center text-amber-600 shadow-inner group-hover:scale-110 transition-transform">
                <Pill className="w-7 h-7" />
              </div>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full text-xs font-bold bg-amber-100/80 text-amber-800 border border-amber-200">
                <Users className="w-3 h-3" />
                {t.problem.card2.metric}
              </span>
            </div>

            <span className="text-xs font-bold uppercase tracking-wider text-amber-600 mb-2 block">
              {t.problem.card2.tag}
            </span>
            <h3 className="text-2xl font-bold text-medical-navy mb-4">
              {t.problem.card2.title}
            </h3>
            <p className="text-gray-600 leading-relaxed text-sm sm:text-base">
              {t.problem.card2.desc}
            </p>
          </div>

          {/* Bento Card 3: Riesgo Legal (Full width on bottom or 3rd column) */}
          <div className="lg:col-span-3 group relative rounded-3xl p-8 sm:p-10 bg-gradient-to-br from-red-50/40 via-white to-gray-50 border border-red-100/80 shadow-glass hover:shadow-glass-lg transition-all duration-300 hover:-translate-y-1">
            <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-6">
              <div className="flex items-center gap-4">
                <div className="w-14 h-14 rounded-2xl bg-red-100 flex items-center justify-center text-medical-danger shadow-inner group-hover:scale-110 transition-transform">
                  <Scale className="w-7 h-7" />
                </div>
                <div>
                  <span className="text-xs font-bold uppercase tracking-wider text-red-600 block">
                    {t.problem.card3.tag}
                  </span>
                  <h3 className="text-2xl font-bold text-medical-navy">
                    {t.problem.card3.title}
                  </h3>
                </div>
              </div>
              <span className="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full text-xs font-bold bg-red-100/80 text-red-800 border border-red-200">
                <TrendingUp className="w-3 h-3" />
                {t.problem.card3.metric}
              </span>
            </div>

            <p className="text-gray-600 leading-relaxed text-base max-w-4xl">
              {t.problem.card3.desc}
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};
