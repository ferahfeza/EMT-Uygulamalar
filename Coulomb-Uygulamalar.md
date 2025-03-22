# Coulomb Kanunu Uygulamaları

## Coulomb Kanunu

Coulomb kanunu, iki yük arasındaki kuvveti hesaplamak için kullanılan bir fizik kanunudur. Coulomb kanunu, iki yük arasındaki kuvveti aşağıdaki formül ile hesaplar:

$$F = k \frac{q_1 q_2}{r^2}$$

Burada:

-$F$, iki yük arasındaki kuvveti,
-$k$, Coulomb sabitini,    
-$q_1$ve$q_2$, iki yükü,
-$d$, iki yük arasındaki mesafeyi temsil eder.

İfadeyi vektörel olarak yazarsak:

$$\mathbf{F} = k \frac{q_1 q_2}{d^2} \mathbf{a}_d$$

Coulomb sabiti$k$değeri, vakumda$8.9875 \times 10^9 \ \text{N m}^2/\text{C}^2$olarak kabul edilir.$\mathbf{a}_d$ise iki yük arasındaki mesafenin birim vektörüdür.$k$ortamın dielektrik sabiti ve Coulomb sabiti arasındaki ilişki aşağıdaki gibidir:

$$k = \frac{1}{4\pi \varepsilon_0}\, \text{(F/m)}$$

Burada$\varepsilon_0$vakumun dielektrik (yalıtkanlık) katsayısıdır ve$8.854 \times 10^{-12} \ \text{F/m}$değerine sahiptir.

## Coulomb Kanunu Uygulamaları

### İki Yük Arasındaki Kuvvetin Hesaplanması

> **Uygulama 1:** Birinci yük$q_1 = 2 \ \text{C}$ve ikinci yük$q_2 = 3 \ \text{C}$olarak kabul edilsin. Birinci yük$(0,0,0)$noktasaında, ikinci yük ise$(3,4,0)$noktasında olsun. İki yük arasındaki kuvveti hesaplayınız.

Çözüm:

İki yük arasındaki mesafe:

$$d = \sqrt{(3-0)^2 + (4-0)^2 + (0-0)^2} = 5 \ \text{m}$$

İki yük arasındaki kuvvet:

$$\mathbf{F} = k \frac{q_1 q_2}{d^2} \mathbf{a}_d = 8.9875 \times 10^9 \cdot  \frac{2  \times 3 \ }{5^2} \mathbf{a}_d$$

Birim vektör$\mathbf{a}_d$'nin hesabı:

$$\mathbf{a}_d = \frac{(3-0)\mathbf{a}_x + (4-0)\mathbf{a}_y + (0-0)\mathbf{a}_z}{5} = 0.6\mathbf{a}_x + 0.8\mathbf{a}_y$$

Bu değeri de yerine yazarsak, sonuç kuvvet vektör değeri aşağıdaki gibi olur:

>$$\mathbf{F} = 8.9875 \times 10^9 \cdot  \frac{2  \times 3 \ }{5^2} (0.6\mathbf{a}_x + 0.8\mathbf{a}_y) = 4.792 \times 10^9 \mathbf{a}_x + 6.389 \times 10^9 \mathbf{a}_y$$

>**Uygulama 2:** Birinci yük$q_1=1\, \text{nC}$, ikinci yük$q_2=2\, \text{nC}$ve üçüncü yük$q_3=-3\, \text{nC}$olarak kabul edilsin. Bu üç yük, sırasıyla$(-2,0,0)$,$(2,0,0)$ve$(0,3,0)$noktalarında olsun. Üçüncü yüke uygulanan kuvveti hesaplayınız.

Çözüm:

Birinci yük ile üçüncü yük arasındaki mesafe:

$$d_1 = \sqrt{(-2-0)^2 + (0-0)^2 + (0-0)^2} = 2 \ \text{m}$$

İkinci yük ile üçüncü yük arasındaki mesafe:

$$d_2 = \sqrt{(2-0)^2 + (0-0)^2 + (0-0)^2} = 2 \ \text{m}$$

Birinci yükün üçüncü yüke uyguladığı kuvvet:

$$\mathbf{F}_1 = k \frac{q_1 q_3}{d_1^2} \mathbf{a}_{d1} = 8.9875 \times 10^9 \cdot  \frac{1  \times -3 \ }{2^2} \mathbf{a}_{d1}$$

$\mathbf{a}_{d1}$birim vektörü birinci yükten üçüncü yüke doğru olmalıdır. Bu vektör aşağıdaki gibi tanımlanır:

$$\mathbf{a}_{d1}=\frac{\mathbf{d1}}{d1}=\frac{(0-(-2)))\mathbf{a}_x+(3-0)\mathbf{a}_y}{\sqrt{2^2+3^2}}=\frac{2\mathbf{a}_x+3\mathbf{a}_y}{\sqrt{13}}$$

Bu değeri de yerine yazarsak, birinci yükün üçüncü yüke uyguladığı kuvvet:

$$\mathbf{F}_1 = 8.9875 \times 10^9 \cdot  \frac{1  \times -3 \ }{2^2} \frac{2\mathbf{a}_x+3\mathbf{a}_y}{\sqrt{13}} = -1.343 \times 10^9 \mathbf{a}_x - 2.015 \times 10^9 \mathbf{a}_y$$

İkinci yükün üçüncü yüke uyguladığı kuvvet:

$$\mathbf{F}_2 = k \frac{q_2 q_3}{d_2^2} \mathbf{a}_{d2} = 8.9875 \times 10^9 \cdot  \frac{2  \times -3 \ }{2^2} \mathbf{a}_{d2}$$

$\mathbf{a}_{d2}$birim vektörü ikinci yükten üçüncü yüke doğru olmalıdır. Bu vektör aşağıdaki gibi tanımlanır:

$$\mathbf{a}_{d2}=\frac{\mathbf{d2}}{d2}=\frac{(0-2)\mathbf{a}_x+(3-0)\mathbf{a}_y}{\sqrt{2^2+3^2}}=\frac{-2\mathbf{a}_x+3\mathbf{a}_y}{\sqrt{13}}$$

Bu değeri de yerine yazarsak, ikinci yükün üçüncü yüke uyguladığı kuvvet:

$$\mathbf{F}_2 = 8.9875 \times 10^9 \cdot  \frac{2  \times -3 \ }{2^2} \frac{-2\mathbf{a}_x+3\mathbf{a}_y}{\sqrt{13}} = -2.686 \times 10^9 \mathbf{a}_x + 4.029 \times 10^9 \mathbf{a}_y$$

Üçüncü yüke uygulanan toplam kuvvet:

$$\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2 = (-1.343 \times 10^9 - 2.686 \times 10^9) \mathbf{a}_x + (-2.015 \times 10^9 + 4.029 \times 10^9) \mathbf{a}_y$$

>$$\mathbf{F} =-4.029 \times 10^9 \mathbf{a}_x + 2.014 \times 10^9 \mathbf{a}_y$$

>**Uygulama 3:**$$\dfrac{x^2}{1} + \dfrac{y^2}{4} = 1$$elipsi ile$y=x$doğrusunun kesişim noktalarına$q_1=1\, \text{nC}$ve$q_2=2\, \text{nC}$yükleri yerleştirilmiştir. Bu iki yük arasındaki kuvveti hesaplayınız.

Çözüm:

Birinci yük ikinci bölgedeki kesişim noktasında, ikinci yükün ise dördüncü bölgedeki kesişim noktasında yerleştiğini varsayalım.

Elipsin denklemi:

$$\dfrac{x^2}{1} + \dfrac{y^2}{4} = 1$$

Doğrunun denklemi:

$$y=x$$

Bu iki denklemin kesişim noktaları:

$$x^2 + 4x^2 = 1$$

$$5x^2 = 1$$

$$x = \pm \dfrac{1}{\sqrt{5}}$$

Bu değerleri yerine yazarsak, kesişim noktaları:

$$x = \pm \dfrac{1}{\sqrt{5}}$$

$$y = \pm \dfrac{1}{\sqrt{5}}$$

İlk yükün koordinatları:

$$q_1 = \left(\dfrac{1}{\sqrt{5}}, \dfrac{1}{\sqrt{5}}\right)$$

İkinci yükün koordinatları:

$$q_2 = \left(-\dfrac{1}{\sqrt{5}}, -\dfrac{1}{\sqrt{5}}\right)$$

İki yük arasındaki mesafe:

$$d = \sqrt{\left(-\dfrac{1}{\sqrt{5}} - \dfrac{1}{\sqrt{5}}\right)^2 + \left(-\dfrac{1}{\sqrt{5}} - \dfrac{1}{\sqrt{5}}\right)^2} = \sqrt{\dfrac{4}{5}} = \dfrac{2}{\sqrt{5}}$$

İki yük arasındaki kuvvet:

$$\mathbf{F} = k \frac{q_1 q_2}{d^2} \mathbf{a}_d = 8.9875 \times 10^9 \cdot  \frac{1  \times 2 \ }{\left(\dfrac{2}{\sqrt{5}}\right)^2} \mathbf{a}_d$$

Birim vektör$\mathbf{a}_d$'nin hesabı:

$$\mathbf{a}_d = \frac{\left(-\dfrac{1}{\sqrt{5}} - \dfrac{1}{\sqrt{5}}\right)\mathbf{a}_x + \left(-\dfrac{1}{\sqrt{5}} - \dfrac{1}{\sqrt{5}}\right)\mathbf{a}_y}{\dfrac{2}{\sqrt{5}}} = -\dfrac{2}{\sqrt{5}}\mathbf{a}_x - \dfrac{2}{\sqrt{5}}\mathbf{a}_y$$

Bu değeri de yerine yazarsak, sonuç kuvvet vektör değeri aşağıdaki gibi olur:

$$\mathbf{F} = 8.9875 \times 10^9 \cdot  \frac{1  \times 2 \ }{\left(\dfrac{2}{\sqrt{5}}\right)^2} \left(-\dfrac{2}{\sqrt{5}}\mathbf{a}_x - \dfrac{2}{\sqrt{5}}\mathbf{a}_y\right)$$
>$$\mathbf{F}  = -1.7985 \times 10^9 \mathbf{a}_x - 1.7985 \times 10^9 \mathbf{a}_y\, \text{(N)}$$

## 










   