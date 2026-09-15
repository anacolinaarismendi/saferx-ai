"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { ShieldCheck, Lock, FileCheck2, Network, CheckCircle } from "lucide-react";

export const ComplianceSection: React.FC = () => {
  const { t } = useLanguage();

  const standards = [
    {
      icon: <Lock className="w-6 h-6 text-medical-blue" />,
      title: t.compliance.hipaaTitle,
      desc: t.compliance.hipaaDesc,
      tag: "USA & Global",
    },
    {
      icon: <ShieldCheck className="w-6 h-6 text-emerald-600" />,
      title: t.compliance.gdprTitle,
      desc: t.compliance.gdprDesc,
      tag: "European Union",
    },
    {
      icon: <FileCheck2 className="w-6 h-6 text-sky-600" />,
      title: t.compliance.fdaEmaTitle,
      desc: t.compliance.fdaEmaDesc,
      tag: "Regulatory Evidence",
    },
    {
      icon: <Network className="w-6 h-6 text-indigo-600" />,
      title: t.compliance.fhirTitle,
      desc: t.compliance.fhirDesc,
      tag: "Interoperability",
    },
  ];

  return (
    <section id="seguridad" className="py-24 bg-white relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-blue-50 border border-blue-100 text-medical-blue text-xs font-bold uppercase tracking-wider mb-4">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>{t.compliance.tag}</span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-medical-navy tracking-tight leading-tight">
            {t.compliance.title}
          </h2>
          <p className="mt-4 text-base sm:text-lg text-gray-600">
            {t.compliance.subtitle}
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {standards.map((item, idx) => (
            <div
              key={idx}
              className="p-7 rounded-2xl bg-gray-50/70 border border-gray-100 shadow-sm hover:shadow-md transition-all duration-300 hover:-translate-y-1"
            >
              <div className="flex items-center justify-between mb-5">
                <div className="w-12 h-12 rounded-xl bg-white flex items-center justify-center shadow-sm border border-gray-100">
                  {item.icon}
                </div>
                <span className="text-[10px] font-bold uppercase tracking-wider bg-white px-2.5 py-1 rounded-md text-gray-500 border border-gray-200">
                  {item.tag}
                </span>
              </div>
              <h3 className="text-lg font-bold text-medical-navy mb-2">
                {item.title}
              </h3>
              <p className="text-sm text-gray-600 leading-relaxed">
                {item.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};
