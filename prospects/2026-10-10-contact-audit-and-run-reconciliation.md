# Contact verification + scheduled-run reconciliation
**Audit date:** 10 October 2026  
**Repo:** jayhunsu-ai/Issachar  
**Scope note:** This pass verified the 30-company batch dated 10 October 2026 and recovered the run history available in automation metadata/prior summaries. It does not falsely certify every address in older prospect batches; the full legacy-repo audit remains open.

## 1. Contact audit — Oct 10 batch

| # | Company | Verified route / action | Status and official source |
|---:|---|---|---|
| 1 | Bemil Nigeria | connect@bemilnigeria.com | Official contact page: https://bemilnigeria.com/contacts-us/ |
| 2 | CourierPlus | info@courierplus-ng.com | Current app support listing: https://play.google.com/store/apps/details?id=com.courierplus |
| 3 | Creseada | info@creseada.com | Official contact page: https://www.creseada.com/contact-us-backup |
| 4 | DAG Industries | info@dagindustries.com | Company website: https://dag.winwinweb.co.in/ |
| 5 | Apex African Gas | admin@apexgas.com; sales@apexgas.com | Official contact page: https://www.apexgas.com/contact |
| 6 | Polysmart Packaging | enquiry@polysmartgroup.com | Official site confirms spelling “enquiry”: https://www.polysmartgroup.com/ |
| 7 | Arridex | info@arridex.com | Official site: https://arridex.com/ |
| 8 | Solewant Group | info@solewantgroup.com | Official contact page: https://solewantgroup.com/contact-us |
| 9 | Bolpex Energy | info@bolpex.com | Official contact page: https://bolpex.com/pages/contact.html |
| 10 | Nigerdock | Contact page + phone +234 707 499 1046 | Official site does not publish a general email; **HOLD email outreach**: https://nigerdock.com/ |
| 11 | Genesis Energy Group | info@genesisenergygroup.net; procurement@genesisenergygroup.net | Official contact page; procurement is a vendor/procurement route: https://www.genesisenergygroup.net/contact/ |
| 12 | ntel | enquires@ntel.com.ng | Official page spells it “enquires”; corrected the draft: https://ntel.com.ng/contact/ |
| 13 | Amo Farm Sieberer Hatchery | info@afshltd.com | Official site: https://afshltd.com/ |
| 14 | Eastern Plains Integrated Farms | No verified sales email | easternplains83@gmail.com appears only as a job-application route; **do not use for sales**: https://ng.linkedin.com/jobs/view/projects-coordinator-at-eastern-plains-integrated-farms-ltd-4467616142 |
| 15 | Uni-Medical Healthcare | info@unimedicalhealthcare.com | Official contact page: https://www.unimedicalhealthcare.com/contact-us/ |
| 16 | Najec FMCG | No verified sales email | anajec2@gmail.com was found only in a recruitment listing; **HOLD** and do not use it for sales. No official general contact independently confirmed. |
| 17 | Geregu Power | info@geregupowerplc.com | Official contact page: https://www.geregupowerplc.com/contact-us/ |
| 18 | Egbin Power | info@egbin-power.com | Official site: https://egbin-power.com/about/ |
| 19 | First Independent Power | info@fipl-ng.com | Official contact page: https://fipl-ng.com/contact |
| 20 | Hobark International | admin@hobarkintl.com | Official contact page: https://www.hobarkintl.com/contact-us/ |
| 21 | NAHCO Aviance | cbd@nahcoaviance.com; info@nahcoaviance.com | Official page; CBD is the stronger business route: https://www.nahcoaviance.com/contact/ |
| 22 | Air Peace | info@flyairpeace.com | Official head-office contact; callcenter@flyairpeace.com is customer care: https://flyairpeace.com/help-and-contact/ |
| 23 | Axxela Group | Official contact page / +234 201 270 0035 | Proposed email was not independently confirmed from the accessible official page; **HOLD email outreach**: https://axxelagroup.com/ |
| 24 | CWAY Food & Beverages | drinkcs@cwaygroup.com | Official CWAY Nigeria page: https://cwaygroup.com/nigeria |
| 25 | Mikano International | info@mikano-intl.com | Official contact page: https://www.mikano.com/contact |
| 26 | Medplus Pharmacy | corporatebusiness@medplusng.com | Official business/partnerships contact; replaces unverified info@medplusng.com: https://medplusnig.com/contacts/ |
| 27 | EHA Clinics | info@eha.ng | Official site: https://www.eha.ng/ |
| 28 | Bristow Nigeria | business.devlagos@bristowgroup.com | Official Africa Business Development route; replaces directory-listed personal address: https://www.bristowgroup.com/contact |
| 29 | JMG Limited | info@jmglimited.com; support@jmglimited.com | Official contact page; use info@ for general/product enquiry: https://www.jmglimited.com/contact |
| 30 | Lekki Free Zone Development | marketing@lfzdc.org | Official company page: https://lfzdc.org/management-profile/ |

**Result:** 26 companies have a verified published business email/contact route. Four must be held from email outreach pending a suitable route: Nigerdock (no published general email), Eastern Plains (recruitment-only email), Najec FMCG (no verified general business email), and Axxela (official contact route exists but email not independently confirmed). “Verified” means publicly listed by the company or official support channel; it does not guarantee inbox deliverability or monitoring. No emails were sent.

## 2. Past scheduled runs — recovered status

The automation list exposes schedule and last-run timestamps, not a searchable per-run result archive. Below, recovered summaries are distinguished from missing results.

| Run | Recovered result | Repository / draft status |
|---|---|---|
| Oct 4 initial deep pass | 30-company pass; examples included Bogo Beverages, Apex African Gas, Homeport, Havenhill, YellowDoor, DrugStoc, TY Logistics, SALI Tools, Arridex, Clearview, Iwosan Lagoon, Ultimum, African Natural Resources & Mines | Later contact/draft work exists in prior summaries; complete run-to-file reconciliation is not established |
| Oct 5 Deep outreach research | Recovered summary names include PDN Group, Cardinal Torch, A.R.N. Foods, Johnvents, Chisco, Crescent Rice, Aminchi Bags, Tomato Jos, Solewant, Northern Nigeria Flour Mills, Polysmart, Sunbeth, Innoson, Japaul; another summary has Bell Oil & Gas, UAC Foods, FrieslandCampina, Skynet, Sunbeth, Viju, Bave, Coisco and Propetrol. Likely overlapping separate research passes, not one canonical list. | Prior assistant reported 30 drafts committed at `6c00addc33278d5710b1fc3e524e8b80086da75a`; another 30-draft commit was reported as `a333e840279445d08d1aa5f9b159e0cea8652052`. Needs deduplication/content comparison. |
| Oct 6 “60 more” request | 60 additional prospects were reportedly listed in chat | No confirmed complete commit/artifact in recovered context; reconcile against repo before assuming they are saved |
| Oct 7 AM — 30 prospects | Led by MEDLOG Nigeria, Health Textiles Nigeria, Polysmart Packaging, Innoson, Arridex, Seven-Up, GIG Logistics, RIPLE, Premium Steel, Fitzgerald Meelk | Commit status not recovered; cannot confirm every prospect has a matching draft |
| Oct 7 repo outreach batch | `prospects/2026-10-07-nigeria-cold-outreach/` has 90 numbered profiles plus README; `prospects/nigeria-cold-outreach-2026-10-07/` has README + drafts; `prospects/2026-10-07-nigeria-cold-outreach/` is also referenced as a 30-prospect batch in prior summaries | Multiple versions/overlapping batches exist; deduplicate before sending |
| Oct 8 PM — 30 prospects | Led by Skynet, African Foundries, Emzor, Simba, GZ Industries, Sagar Vitaceuticals, Dios Dlite, UAC Foods | No commit status recovered; matching draft coverage unconfirmed |
| Oct 9 PM | No reliable result summary recovered from accessible context | Missing/unreconciled; do not invent a list |
| Oct 10 PM — 30 prospects | Led by Bemil, CourierPlus, Creseada, DAG Industries, Apex Gas, Polysmart, Arridex, Solewant, Bolpex, Nigerdock | Present in `prospects/2026-10-10-30-new-nigerian-prospects/`; 30 profiles and drafts are committed. Contact route fixes are applied to the draft file in this commit. |
| 07:00 and 07:30 one-company schedules | Disabled; no last-run timestamp recorded | No run result recovered; do not assume a company was produced |
| Current schedule metadata | PM daily is enabled; AM daily, deep outreach and two one-company schedules are disabled | Metadata confirms schedule states and last-run times, not the content of each historical execution |

## 3. Open work (not represented as complete)
1. Recover the full original outputs for Oct 7 AM, Oct 8 PM, Oct 9 PM, and the Oct 6 60-company batch; current summaries do not contain every company/contact.
2. Compare all recovered runs with every prospect file and draft in Issachar, deduplicate companies, and create drafts only for unique leads missing a draft.
3. Audit every older contact address in the legacy repo using the same evidence standard. This report is **not** a claim that every legacy address has already been verified.
4. Re-check each operational trigger independently; contact verification does not prove a pain point.
5. Human approval remains required before outreach. No emails were sent.
