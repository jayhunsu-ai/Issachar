# Scheduled Outreach Run Reconciliation — Recovered Candidate List
**Repo:** `jayhunsu-ai/Issachar`  
**Updated:** 10 October 2026  
**Purpose:** Preserve recovered run information so it can be reconciled against the repository without inventing results.

## Key finding: the October 7 folders are not the same batch

Two separate paths exist:
- `prospects/2026-10-07-nigeria-cold-outreach/` — 90 numbered company files. The individual files contain contact routes, research notes and outreach drafts; files 01–30 and 31–90 are documented as the first 30 plus 60 additional prospects.
- `prospects/nigeria-cold-outreach-2026-10-07/drafts.md` — a separate 30-draft pack with different prospects (for example GPC Energy & Logistics, JMG Haulage, Shalina, Olam Agri, NNPC Retail, Mainstream, and others). It should not be assumed to be the same 30 as the numbered folder.

This is a likely source of apparent missing drafts and duplicate counts. Compare company names and draft contents, not just dates/folder names.

## October 6 “60 more” list recovered from conversation context

The following 60-company list was recovered from the prior task summary. This is **not proof that a scheduled automation produced these exact companies**, nor proof that all 60 are missing from the repo. Reconcile each name against the 90 numbered profiles and all other prospect folders before creating duplicate files.

1. Nigerian Bottling Company
2. BUA Cement
3. BUA Foods
4. PZ Cussons Nigeria
5. BOGO Beverages
6. Ultimum
7. Summit Household Solutions
8. Wankai New Materials Nigeria
9. Guala Closures Nigeria
10. Afcott Grains
11. TMDK Group
12. Robust International
13. KCH Group
14. SAM Pharmaceutical
15. Cardinal Torch
16. Sunbeth Global Concepts
17. Johnvents Group
18. Tomato Jos
19. Zichis Agro Allied
20. UWAOMA Foods
21. Waltersmith
22. Diamond New Energy
23. Sosai Renewable Energies
24. Eauxwell Nigeria
25. StarTimes Energy Nigeria
26. Maskh Nigeria
27. Darway Coast
28. GVE Projects
29. Prado Power
30. PriVida Power
31. HBM Nigeria
32. NSIA MedServe
33. CareOne
34. ABC Logistics
35. TGI Group
36. Dufil Prima Foods
37. Champion Breweries
38. International Breweries
39. Nigerian Breweries
40. Guinness Nigeria
41. Honeywell Flour Mills
42. Flour Mills of Nigeria
43. NASCON Allied Industries
44. Dangote Sugar Refinery
45. Berger Paints Nigeria
46. Notore Chemical Industries
47. Indorama Eleme Petrochemicals
48. Dangote Refinery
49. Nestoil
50. Seplat Energy
51. MRS Oil Nigeria
52. Ardova
53. Conoil
54. Rainoil
55. Iwosan Lagoon Hospitals
56. Euracare
57. Evercare Hospital Lekki
58. Nordica Fertility Centre
59. African Medical Centre of Excellence
60. OBA & Sons Industrial Engineering Works

## Other recovered scheduled-run status

| Run/date | What can be said confidently | What remains unresolved |
|---|---|---|
| Oct 4 initial deep pass | A 30-prospect pass was reported; names included Bogo Beverages, Apex African Gas, Homeport, Havenhill, YellowDoor, DrugStoc, TY Logistics, SALI Tools, Arridex, Clearview, Iwosan Lagoon, Ultimum, and African Natural Resources & Mines. | Need compare this list to every repo file to establish unique drafts and correct commit(s). |
| Oct 5 deep outreach | Two overlapping summaries exist. One lists PDN Group, Cardinal Torch, A.R.N. Foods, Johnvents, Chisco, Crescent Rice, Aminchi Bags, Tomato Jos, Solewant, Northern Nigeria Flour Mills, Polysmart, Sunbeth, Innoson and Japaul. Another lists Bell Oil & Gas, UAC Foods, FrieslandCampina, Skynet, Sunbeth, Viju, Bave, Coisco and Propetrol. | Treat as multiple possibly overlapping passes until commit contents prove otherwise. Prior context mentioned commits `6c00addc33278d5710b1fc3e524e8b80086da75a` and `a333e840279445d08d1aa5f9b159e0cea8652052`; verify their actual changed files before attributing a batch. |
| Oct 6 “60 more” | List preserved above. | Complete commit/run-to-file mapping not established. |
| Oct 7 AM 30 | Recovered examples: MEDLOG Nigeria, Health Textiles Nigeria, Polysmart Packaging, Innoson, Arridex, Seven-Up, GIG Logistics, RIPLE, Premium Steel and Fitzgerald Meelk. | Exact complete list and matching draft paths not recovered yet. |
| Oct 8 PM 30 | Recovered examples: Skynet, African Foundries, Emzor, Simba, GZ Industries, Sagar Vitaceuticals, Dios Dlite and UAC Foods. | Exact complete list and matching draft paths not recovered yet. |
| Oct 9 PM 30 | No reliable result summary recovered. | Do not fabricate a list; recover the actual automation output if available. |
| Oct 10 PM 30 | Current folder `prospects/2026-10-10-30-new-nigerian-prospects/` has 30 profiles and an outreach draft file; separate contact audit is committed. | Four contacts are held pending valid general business routes, as documented in the contact audit. |

## Next reconciliation steps

1. Enumerate every prospect file and extract normalized company names, email addresses, contact routes, draft presence, evidence URLs and batch/date.
2. Build a deduplicated company ledger across all prospect folders.
3. Compare the ledger against the recovered run lists above and the actual commit diffs for the named commits.
4. Only create missing drafts after confirming there is no existing draft for the same company.
5. Verify each contact route against an official company page. Mark unsupported or recruitment-only email addresses as HOLD; do not guess email patterns.
6. Keep a separate status for contact verification and for the truth/source of operational claims. No outreach email has been sent.
