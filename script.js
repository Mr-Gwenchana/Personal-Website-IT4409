document.addEventListener("DOMContentLoaded", () => {
    // Theme Switch Logic
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    const currentTheme = localStorage.getItem('theme');

    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);
        if (currentTheme === 'light') {
            toggleSwitch.checked = true;
        }
    }

    function switchTheme(e) {
        if (e.target.checked) {
            document.documentElement.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        }    
    }

    toggleSwitch.addEventListener('change', switchTheme, false);

    const hobbyCards = document.querySelectorAll('.hobby-card');
    const detailCards = document.querySelectorAll('.detail-card');
    const paths = document.querySelectorAll('.sig-path');
    
    // Initialize paths
    paths.forEach(path => {
        const length = path.getTotalLength();
        path.style.strokeDasharray = length;
        path.style.strokeDashoffset = length;
    });
    
    // Scroll logic for sections
    window.addEventListener('scroll', () => {
        // Details section logic
        const detailsSection = document.querySelector('.details-section');
        if (detailsSection) {
            const dTop = detailsSection.offsetTop;
            const dHeight = detailsSection.offsetHeight;
            const windowHeight = window.innerHeight;
            
            const dScrollDistance = dHeight - windowHeight;
            let dProgress = (window.scrollY - dTop) / dScrollDistance;
            
            if (dProgress < 0) dProgress = 0;
            if (dProgress > 1) dProgress = 1;
            
            detailCards.forEach((card, index) => {
                // Determine the scroll window for this specific card
                // Each card takes up roughly 40% of the total scroll, staggered.
                const start = index * 0.15; 
                const end = start + 0.4;
                
                let p = (dProgress - start) / (end - start);
                if (p < 0) p = 0;
                if (p > 1) p = 1;
                
                // p goes from 0 (offscreen right) to 1 (in position)
                card.style.setProperty('--scroll-x', `${(1 - p) * 100}vw`);
                card.style.setProperty('--scroll-opacity', p);
            });
        }

        // Final Section (Hobbies & Signature) logic
        const finalSection = document.querySelector('.final-section');
        if (finalSection) {
            const fTop = finalSection.offsetTop;
            const fHeight = finalSection.offsetHeight;
            const windowHeight = window.innerHeight;
            
            const fScrollDistance = fHeight - windowHeight;
            let fProgress = (window.scrollY - fTop) / fScrollDistance;
            
            if (fProgress < 0) fProgress = 0;
            if (fProgress > 1) fProgress = 1;

            // Phase 1: 0.0 to 0.35 (Hobbies Cards fade in)
            // Phase 2: 0.35 to 0.5 (Crossfade Hobbies to Signature)
            // Phase 3: 0.5 to 1.0 (Draw Signature)

            // Phase 1
            const hobbiesPhase = Math.min(1, Math.max(0, fProgress / 0.35));
            hobbyCards.forEach((card, index) => {
                const start = index * 0.15; 
                const end = start + 0.4;
                let p = (hobbiesPhase - start) / (end - start);
                if (p < 0) p = 0;
                if (p > 1) p = 1;
                
                if (p > 0.5) {
                    card.classList.add('visible');
                } else {
                    card.classList.remove('visible');
                }
            });

            // Phase 2
            const fadePhase = Math.min(1, Math.max(0, (fProgress - 0.35) / 0.15));
            const sigContainer = document.querySelector('.signature-container');
            const hobbiesContainer = document.querySelector('.hobbies-container');
            
            if (sigContainer && hobbiesContainer) {
                sigContainer.style.opacity = fadePhase;
                hobbiesContainer.style.opacity = 1 - fadePhase;
                
                if (fadePhase > 0) {
                    sigContainer.style.pointerEvents = 'all';
                } else {
                    sigContainer.style.pointerEvents = 'none';
                }
            }

            // Phase 3
            const drawPhase = Math.min(1, Math.max(0, (fProgress - 0.5) / 0.5));
            const totalPaths = paths.length;
            const pathProgress = drawPhase * totalPaths;
            
            paths.forEach((path, index) => {
                const length = path.getTotalLength();
                if (pathProgress > index + 1) {
                    path.style.strokeDashoffset = 0;
                } else if (pathProgress > index) {
                    const p = pathProgress - index;
                    path.style.strokeDashoffset = length * (1 - p);
                } else {
                    path.style.strokeDashoffset = length;
                }
            });
        }
    });
});
