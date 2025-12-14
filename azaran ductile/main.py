from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="fa" dir="rtl" class="scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        
        <title>آذران تک تجارت هامون | شمش چدن داکتیل</title>
        <meta name="description" content="تأمین کننده شمش چدن داکتیل با آنالیز دقیق برای صنایع ریخته‌گری و خودروسازی.">
        
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
        
        <style>
            body { font-family: 'Vazirmatn', sans-serif; background-color: #020617; color: #f1f5f9; }
            
            /* Glassmorphism */
            .glass-panel {
                background: rgba(15, 23, 42, 0.6);
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            
            /* Mobile Menu Animation */
            #mobile-menu {
                transition: all 0.3s ease-in-out;
                transform-origin: top;
            }
            .menu-hidden {
                opacity: 0;
                transform: scaleY(0);
                height: 0;
            }
            .menu-visible {
                opacity: 1;
                transform: scaleY(1);
                height: auto;
            }

            .phone-number {
                direction: ltr;
                font-family: monospace;
            }
        </style>
    </head>
    <body class="overflow-x-hidden selection:bg-orange-500 selection:text-white">

        <nav class="fixed w-full z-50 top-0 glass-panel border-b border-white/5">
            <div class="container mx-auto px-4 md:px-6 py-4">
                <div class="flex justify-between items-center">
                    <a href="#" class="text-xl md:text-2xl font-black tracking-widest text-white z-50">
                        AZARAN <span class="text-orange-500">TAK</span>
                    </a>

                    <div class="hidden md:flex gap-8 text-sm font-medium text-gray-300 items-center">
                        <a href="#features" class="hover:text-orange-400 transition">ویژگی‌ها</a>
                        <a href="#specs" class="hover:text-orange-400 transition">آنالیز فنی</a>
                        <a href="#applications" class="hover:text-orange-400 transition">کاربردها</a>
                        <a href="#contact" class="px-5 py-2 bg-orange-600 hover:bg-orange-700 text-white rounded-full transition shadow-lg shadow-orange-600/20">تماس با ما</a>
                    </div>

                    <button id="menu-btn" class="md:hidden text-white focus:outline-none z-50">
                        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>

                <div id="mobile-menu" class="menu-hidden md:hidden flex flex-col items-center gap-4 mt-4 pb-4 border-t border-white/10 pt-4">
                    <a href="#features" class="text-gray-300 hover:text-white py-2 w-full text-center" onclick="toggleMenu()">ویژگی‌ها</a>
                    <a href="#specs" class="text-gray-300 hover:text-white py-2 w-full text-center" onclick="toggleMenu()">آنالیز فنی</a>
                    <a href="#applications" class="text-gray-300 hover:text-white py-2 w-full text-center" onclick="toggleMenu()">کاربردها</a>
                    <a href="#contact" class="px-8 py-3 bg-orange-600 text-white rounded-xl w-full text-center shadow-lg" onclick="toggleMenu()">تماس با ما</a>
                </div>
            </div>
        </nav>

        <header class="relative min-h-screen flex items-center justify-center pt-20 overflow-hidden px-4">
            <div class="absolute inset-0 z-0">
                <img src="https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?q=80&w=2070&auto=format&fit=crop" 
                     class="w-full h-full object-cover opacity-30 animate-[pulse_8s_ease-in-out_infinite]" alt="Foundry">
                <div class="absolute inset-0 bg-gradient-to-t from-[#020617] via-[#020617]/70 to-transparent"></div>
            </div>

            <div class="container mx-auto relative z-10 text-center">
                <span class="inline-block py-1 px-3 rounded-full bg-orange-500/10 border border-orange-500/20 text-orange-400 text-xs font-bold mb-6 tracking-widest uppercase">
                    استاندارد جهانی ISO
                </span>
                
                <h1 class="text-5xl sm:text-6xl md:text-8xl font-black text-white mb-6 leading-tight">
                    شمش چدن <br class="hidden md:block" />
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-red-600">داکتیل</span>
                </h1>
                
                <p class="text-lg md:text-xl text-gray-300 max-w-2xl mx-auto mb-10 font-light leading-relaxed px-4">
                    تأمین پایدار مواد اولیه ریخته‌گری با ساختار گرافیت کروی و ضمانت آنالیز شیمیایی
                </p>
                
                <div class="flex flex-col sm:flex-row justify-center gap-4 px-4 w-full sm:w-auto">
                    <a href="#contact" class="w-full sm:w-auto px-8 py-4 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl transition shadow-orange-900/50 shadow-xl text-center">
                        ثبت سفارش
                    </a>
                    <a href="#specs" class="w-full sm:w-auto px-8 py-4 glass-panel text-white font-bold rounded-xl hover:bg-white/10 transition text-center">
                        مشاهده جدول
                    </a>
                </div>
            </div>
        </header>

        <section id="specs" class="py-20 bg-[#020617] relative">
            <div class="container mx-auto px-4 md:px-6 relative z-10">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-start">
                    
                    <div class="order-2 lg:order-1">
                        <h2 class="text-3xl md:text-4xl font-bold text-white mb-6 border-r-4 border-orange-500 pr-4">
                            چرا چدن داکتیل آذران؟
                        </h2>
                        <p class="text-gray-400 leading-loose mb-8 text-justify">
                            شمش‌های ما با کنترل دقیق میزان منیزیم و فرآیند تلقیح استاندارد تولید می‌شوند. این یعنی شما گرافیت‌های کاملاً کروی دارید که باعث می‌شود قطعات نهایی شما نشکن باشند و در برابر فشارهای مکانیکی خرد نشوند.
                        </p>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div class="glass-panel p-4 rounded-xl flex items-center gap-3">
                                <span class="text-2xl">🧬</span>
                                <span class="text-sm text-gray-300">ساختار میکروسکوپی دقیق</span>
                            </div>
                            <div class="glass-panel p-4 rounded-xl flex items-center gap-3">
                                <span class="text-2xl">🔨</span>
                                <span class="text-sm text-gray-300">ماشین‌کاری عالی</span>
                            </div>
                            <div class="glass-panel p-4 rounded-xl flex items-center gap-3">
                                <span class="text-2xl">⚖️</span>
                                <span class="text-sm text-gray-300">تضمین وزن و آنالیز</span>
                            </div>
                            <div class="glass-panel p-4 rounded-xl flex items-center gap-3">
                                <span class="text-2xl">📦</span>
                                <span class="text-sm text-gray-300">ارسال به تمام نقاط</span>
                            </div>
                        </div>
                    </div>

                    <div class="order-1 lg:order-2 glass-panel p-1 rounded-2xl shadow-2xl">
                        <div class="bg-[#0f172a]/80 backdrop-blur rounded-xl p-6 overflow-x-auto">
                            <h3 class="text-xl font-bold text-white mb-4 flex items-center justify-between min-w-[300px]">
                                آنالیز شیمیایی
                                <span class="text-xs bg-green-500/20 text-green-400 px-2 py-1 rounded border border-green-500/30">Verified</span>
                            </h3>
                            <table class="w-full min-w-[300px]">
                                <tbody class="divide-y divide-white/10 text-sm md:text-base">
                                    <tr class="hover:bg-white/5"><td class="py-3 text-gray-400">کربن (C)</td><td class="py-3 text-left font-mono text-orange-400 font-bold dir-ltr">3.5 - 4.5 %</td></tr>
                                    <tr class="hover:bg-white/5"><td class="py-3 text-gray-400">سیلیسیم (Si)</td><td class="py-3 text-left font-mono text-gray-300 dir-ltr">Max 1.0 %</td></tr>
                                    <tr class="hover:bg-white/5"><td class="py-3 text-gray-400">منگنز (Mn)</td><td class="py-3 text-left font-mono text-gray-300 dir-ltr">0.5 %</td></tr>
                                    <tr class="hover:bg-white/5"><td class="py-3 text-gray-400">فسفر (P)</td><td class="py-3 text-left font-mono text-gray-300 dir-ltr">Max 0.2 %</td></tr>
                                    <tr class="hover:bg-white/5"><td class="py-3 text-gray-400">گوگرد (S)</td><td class="py-3 text-left font-mono text-gray-300 dir-ltr">0.1 %</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="applications" class="py-20 bg-[#050b1e]">
            <div class="container mx-auto px-4 md:px-6">
                <div class="text-center mb-12">
                    <h2 class="text-3xl md:text-5xl font-bold text-white">کاربردهای صنعتی</h2>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="group relative h-64 rounded-2xl overflow-hidden cursor-pointer shadow-lg">
                        <img src="https://images.unsplash.com/photo-1486262715619-67b85e0b08d3?q=80&w=800" class="absolute inset-0 w-full h-full object-cover transition duration-700 group-hover:scale-110" alt="Car Engine">
                        <div class="absolute inset-0 bg-black/50 group-hover:bg-black/40 transition"></div>
                        <div class="absolute bottom-5 right-5 text-white">
                            <h3 class="text-xl font-bold">خودروسازی</h3>
                            <p class="text-sm text-gray-300">بلوک سیلندر و شاتون</p>
                        </div>
                    </div>
                    <div class="group relative h-64 rounded-2xl overflow-hidden cursor-pointer shadow-lg">
                        <img src="https://images.unsplash.com/photo-1542013936693-884638332954?q=80&w=800" class="absolute inset-0 w-full h-full object-cover transition duration-700 group-hover:scale-110" alt="Pipes">
                        <div class="absolute inset-0 bg-black/50 group-hover:bg-black/40 transition"></div>
                        <div class="absolute bottom-5 right-5 text-white">
                            <h3 class="text-xl font-bold">لوله و اتصالات</h3>
                            <p class="text-sm text-gray-300">اتصالات آب و گاز</p>
                        </div>
                    </div>
                    <div class="group relative h-64 rounded-2xl overflow-hidden cursor-pointer shadow-lg border border-orange-500/40">
                        <img src="https://images.unsplash.com/photo-1579567761406-4684ee0c75b6?q=80&w=800" class="absolute inset-0 w-full h-full object-cover transition duration-700 group-hover:scale-110 grayscale group-hover:grayscale-0" alt="Excavator">
                        <div class="absolute inset-0 bg-black/50 group-hover:bg-black/40 transition"></div>
                        <div class="absolute bottom-5 right-5 text-white">
                            <h3 class="text-xl font-bold text-orange-400">ماشین‌آلات سنگین</h3>
                            <p class="text-sm text-gray-300">قطعات ضدسایش</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <footer id="contact" class="py-16 md:py-24 bg-[#020617] border-t border-white/5">
            <div class="container mx-auto px-4 md:px-6">
                <div class="glass-panel rounded-3xl p-6 md:p-12 shadow-2xl">
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
                        
                        <div class="text-center lg:text-right">
                            <h2 class="text-3xl md:text-4xl font-black text-white mb-4">همکاری با ما</h2>
                            <p class="text-gray-400 leading-loose mb-6">
                                جهت استعلام قیمت روز و دریافت پیش‌فاکتور رسمی، با واحد بازرگانی تماس بگیرید.
                            </p>
                            <a href="mailto:azarantak.test@gmail.com" class="inline-flex items-center gap-2 bg-white/5 border border-white/10 px-4 py-2 rounded-lg text-gray-300 hover:text-white hover:bg-white/10 transition">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
                                azarantak.test@gmail.com
                            </a>
                        </div>

                        <div class="bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl p-6 border border-white/10 flex items-center gap-4 hover:border-orange-500/50 transition">
                            <div class="w-14 h-14 rounded-full bg-orange-600 flex items-center justify-center shrink-0 text-2xl">📞</div>
                            <div class="w-full">
                                <p class="text-orange-500 text-xs font-bold uppercase mb-1">مدیر عامل</p>
                                <h3 class="text-lg font-bold text-white">بهمن آبجو</h3>
                                <div class="flex justify-end dir-ltr w-full">
                                    <a href="tel:+989150119347" class="phone-number text-xl md:text-2xl font-bold text-white hover:text-orange-400 transition block w-full text-right">
                                        +98 915 011 9347
                                    </a>
                                </div>
                            </div>
                        </div>

                    </div>
                    
                    <div class="mt-10 pt-6 border-t border-white/5 text-center text-xs text-gray-500">
                        <p>© 2025 Azaran Tak Tejarat Hamoon</p>
                        <p class="mt-1">زاهدان، بلوار جانبازان، کوچه شقایق، بن‌بست میلاد</p>
                    </div>
                </div>
            </div>
        </footer>

        <script>
            const btn = document.getElementById('menu-btn');
            const menu = document.getElementById('mobile-menu');

            function toggleMenu() {
                if (menu.classList.contains('menu-hidden')) {
                    menu.classList.remove('menu-hidden');
                    menu.classList.add('menu-visible');
                } else {
                    menu.classList.remove('menu-visible');
                    menu.classList.add('menu-hidden');
                }
            }

            btn.addEventListener('click', toggleMenu);
        </script>

    </body>
    </html>
    """
    return html_content