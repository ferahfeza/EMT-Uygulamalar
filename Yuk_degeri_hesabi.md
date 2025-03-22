# Yük Dağılımlarının İhtiva ettiği Toplam Yük Değerlerinin Hesaplanması

## Çizgisel Yük Dağılımlarının İhtiva ettiği Toplam Yük Değeri

Çizgisel bir hat boyunca tanımlanmış bir yük yoğunluğu düşünelim. Bu yük yoğunluğunu $\lambda$ ile gösterelim. Bu durumda, bu çizgisel yük dağılımı üzerinde bir diferansiyel yük miktarı aşağıdaki gibi ifade edilir:

$$dq = \lambda \, dl$$

Burada $dl$ çizgisel yük dağılımının birim uzunluğunu temsil eder. Bu durumda, bu çizgisel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:

$$Q = \int dq = \int \lambda \, dl$$

Bu integrali çözmek için,$dl$ifadesini uygun bir şekilde ifade etmek gerekmektedir. Kartezyen koordinat sisteminde$dl$ifadesi aşağıdaki gibi ifade edilir:

$$dl = \sqrt{dx^2 + dy^2 + dz^2} = \sqrt{1 + \left(\frac{dy}{dx}\right)^2 + \left(\frac{dz}{dx}\right)^2} \, dx$$

Bu durumda, çizgisel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:

$$Q = \int \lambda \, dl = \int \lambda \sqrt{1 + \left(\frac{dy}{dx}\right)^2 + \left(\frac{dz}{dx}\right)^2} \, dx$$

Bir örnek verelim:

> **Uygulama 1:** Bir çizgisel yük dağılımı, $y = x^2$ eğrisi üzerinde, $\lambda=x\, \text{(C/m)}$ değeri ile tanımlanmıştır. $0 \leq x \leq 1$ aralığındaki toplam yük miktarını hesaplayınız.
>
> **Çözüm:**
>
> Çizgisel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:
>
>$$Q = \int \lambda \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx = \int_0^1 x \sqrt{1 + 4x^2} \, dx$$
>
> Bu integrali çözmek için, $u = 1 + 4x^2$ değişken dönüşümü yapalım. Bu durumda, $du = 8x \, dx$ olur. Bu durumda integral aşağıdaki gibi ifade edilir:
>
>$$Q = \int \frac{1}{8} \sqrt{u} \, du = \frac{1}{8} \cdot \frac{2}{3} u^{3/2} = \frac{1}{12} u^{3/2} = \frac{1}{12} (1 + 4x^2)^{3/2} \Bigg|_0^1$$$$= \frac{1}{12} (5^{3/2} - 1) = \frac{5\sqrt{5} - 1}{12} \, \text{C}$$


>**Uygulama 2:** $x^2+y^2=a^2$ çemberi üzerinde yük yoğunluğu $\lambda=a^2\sin3\phi\, \text{(C/m)}$ olan bir çizgisel yük dağılımı düşünelim. Çember üzerindeki toplam yük miktarını hesaplayınız.

>**Çözüm:** Çizgisel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:

> Çember üzerinde tanımlanan diferansiyel uzunluk$dl$ifadesi aşağıdaki gibi ifade edilir:
>
>$$dl=ad\phi$$
>
> Bu durumda, çizgisel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:
>
>$$Q = \int \lambda \, dl = \int a^2\sin3\phi \cdot a \, d\phi = a^3 \int \sin3\phi \, d\phi$$
>
> Bu integrali çözmek için, trigonometrik dönüşüm yapalım. Bu durumda, integral aşağıdaki gibi ifade edilir:
>
>$$Q = a^3 \int \sin3\phi \, d\phi = -\frac{a^3}{3} \cos3\phi \Bigg|_0^{\pi} = -\frac{a^3}{3} (\cos3\pi - \cos0)$$
>$$Q = -\frac{a^3}{3} (-1 - 1) = \frac{2a^3}{3} \, \text{C}$$
>
> **Uygulama 3:** $y=sinx$ fonksiyonu üzerinde $\lambda=2x\, \text{(C/m)}$ yük yoğunluğu olan bir çizgisel yük dağılımı düşünelim. $0 \leq x \leq \pi$ aralığındaki toplam yük miktarını hesaplayınız.
>
> **Çözüm:**
>
> Çizgisel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:
>
>$$Q = \int \lambda \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx = \int_0^{\pi} 2x \sqrt{1 + \cos^2x} \, dx$$
>
> Bu integrali çözmek için, $u = 1 + \cos^2x$ değişken dönüşümü yapalım. Bu durumda, $du = -2\cos x \sin x \, dx$ olur. Bu durumda integral aşağıdaki gibi ifade edilir:
>
>$$Q = \int -\frac{1}{2} \sqrt{u} \, du = -\frac{1}{2} \cdot \frac{2}{3} u^{3/2} = -\frac{1}{3} u^{3/2} = -\frac{1}{3} (1 + \cos^2x)^{3/2} \Bigg|_0^{\pi}$$$$= -\frac{1}{3} (2^3 - 1) = -\frac{7}{3} \, \text{C}$$

## Yüzeysel Yük Dağılımlarının İhtiva ettiği Toplam Yük Değeri

Yüzeysel yük dağılımı, bir yüzey üzerinde tanımlanmış bir yük yoğunluğu ile ifade edilir. Bu durumda, bu yüzey yük dağılımı üzerinde bir diferansiyel yük miktarı aşağıdaki gibi ifade edilir:

$$dq = \sigma \, ds$$

Burada $ds$ yüzey yük dağılımının birim alanını temsil eder. Bu durumda, bu yüzey yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:

$$Q = \int dq = \int \sigma \, ds$$

Bu integrali çözmek için,$ds$ifadesini, çalışılan koordinat sistemine uygun bir şekilde ifade etmek gerekmektedir.

>**Uygulama 4:** Yarıçapı$a$olan bir diskin yüzeyinde tanımlanmış bir yüzeysel yük yoğunluğu $\sigma = 3\rho^2\, \text{(C/m}^2)$ olan bir yüzey yük dağılımı düşünelim. Disk üzerindeki toplam yük miktarını hesaplayınız.

>**Çözüm:** Yüzey yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:
> Disk üzerinde tanımlanan diferansiyel alan$ds$ifadesi aşağıdaki gibi ifade edilir:
>
>$$ds_z =\rho d\rho  d\phi$$
>
> Bu durumda, yüzey yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:
>
>$$Q = \int \sigma \, ds = \int_0^a \int_0^{2\pi} 3\rho^2 \cdot \rho d\rho d\phi = 3 \int_0^a \rho^3 d\rho \int_0^{2\pi} d\phi$$
>$$Q = 3 \left[\frac{\rho^4}{4}\right]_0^a \left[\phi\right]_0^{2\pi} = 3 \left[\frac{a^4}{4} - 0\right] \left[2\pi - 0\right]$$
>$$Q = 3 \cdot \frac{a^4}{4} \cdot 2\pi = \frac{3}{2} \pi a^4 \, \text{C}$$

>**Uygulama 5:** Köşe noktaları (0,0,0), (1,0,0) ve (0,1,0) olan bir üçgenin yüzeyinde tanımlanmış bir yüzeysel yük yoğunluğu $\sigma = 2x\, \text{(C/m}^2)$ olan bir yüzey yük dağılımı düşünelim. Üçgen yüzeyindeki toplam yük miktarını hesaplayınız.

>**Çözüm:** 
Köşe noktaları (0,0,0), (1,0,0) ve (0,1,0) olan üçgenin yüzeyindeki toplam yük miktarını bulmak için, yük yoğunluğu $\sigma = 2x \, \text{C/m}^2$'yi üçgenin yüzeyi üzerinde entegre etmemiz gerekmektedir. Üçgen, $xy$ düzleminde yer alan ve $x + y ≤ 1$ koşulunu sağlayan bir bölgedir.
Toplam yük, yük yoğunluğunun bu bölge üzerinde çift katlı integrali alınarak hesaplanır:
$$
Q = \iint\limits_{\text{Üçgen}} \sigma \, dA
$$
Öncelikle integral sınırlarını belirleriz. $x$ 0'dan 1'e kadar değişirken, $y$ 0'dan$1 - x$'e kadar değişir. İntegrali $x$'e göre kurarsak:
$$
Q = \int_{x=0}^{1} \int_{y=0}^{1-x} 2x \, dy \, dx
$$
İç integrali hesaplarsak:
$$
\int_{y=0}^{1-x} 2x \, dy = 2x \left[ y \right]_{0}^{1-x} = 2x (1 - x)
$$
Dış integrali hesaplarsak:
$$
Q = \int_{0}^{1} 2x (1 - x) \, dx = \int_{0}^{1} (2x - 2x^2) \, dx
$$
Bu integrali parçalara ayırıp çözersek:
$$
\int_{0}^{1} 2x \, dx - \int_{0}^{1} 2x^2 \, dx = \left[ x^2 \right]_{0}^{1} - \left[ \frac{2x^3}{3} \right]_{0}^{1} = 1 - \frac{2}{3} = \frac{1}{3}
$$
Aynı sonucu, integral sırasını değiştirerek de doğrulayabiliriz. y 0'dan 1'e kadar değişirken, x 0'dan$1 - y$'e kadar değişir:
$$
Q = \int_{y=0}^{1} \int_{x=0}^{1-y} 2x \, dx \, dy
$$
İç integrali hesaplarsak:
$$
\int_{x=0}^{1-y} 2x \, dx = \left[ x^2 \right]_{0}^{1-y} = (1 - y)^2
$$
Dış integrali hesaplarsak:
$$
Q = \int_{0}^{1} (1 - y)^2 \, dy = \left[ \frac{(1 - y)^3}{3} \right]_{0}^{1} = \frac{1}{3}
$$
Her iki yöntemle de aynı sonuç elde edilir. Bu nedenle, toplam yük miktarı:
$$
\boxed{\dfrac{1}{3}} \, \text{C}
$$

>**Uygulama 6:** Yarıçapı$a$olan bir silindirin yüzeyinde tanımlanmış bir yüzeysel yük yoğunluğu $\sigma = 3\rho^2\, \text{(C/m}^2)$ olan bir yüzey yük dağılımı düşünelim. Silindir yüzeyindeki toplam yük miktarını hesaplayınız.

>**Çözüm:**   
>Toplam yük miktarını hesaplamak için, yüzey yük yoğunluğunu silindirin eğrisel yüzeyi üzerinde integral almalıyız. Silindirin yan yüzeyi için silindirik koordinat sistemi kullanılır. Burada yarıçap$\rho = a$sabit olduğundan, yüzey alan elemanı $ds_r = a \, d\phi \, dz$ şeklinde ifade edilir. Yük yoğunluğu $\sigma = 3\rho^2$ olduğundan ve $\rho = a$ olduğu için $\sigma = 3a^2$ olur.

>**Adımlar:**
>1. **İntegralin Kurulumu:**  
  $$
   Q = \int \sigma \, ds_r = \int_{0}^{2\pi} \int_{0}^{L} 3a^2 \cdot a \, dz \, d\phi
  $$
   Burada$ds_r = a \, d\phi \, dz$olduğu için$3a^2 \cdot a = 3a^3$yazılır.
>2. **İntegralin Hesaplanması:**  
  $$
   Q = 3a^3 \int_{0}^{2\pi} d\phi \int_{0}^{L} dz = 3a^3 \cdot 2\pi \cdot L = 6\pi a^3 L
  $$
>**Sonuç:**  
Toplam yük miktarı $\boxed{6\pi a^3 L} \, \text{C} $olarak bulunur.

>**Uygulama 7:** Yarıçapı$a$olan bir kürenin yüzeyinde tanımlanmış bir yüzeysel yük yoğunluğu $\sigma = 2r\, \text{(C/m}^2)$ olan bir yüzey yük dağılımı düşünelim. Küre yüzeyindeki toplam yük miktarını hesaplayınız.

>**Çözüm:**
>Toplam yük miktarını hesaplamak için, yüzey yük yoğunluğunu kürenin yüzeyi üzerinde integral almalıyız. Kürenin yarıçapı$r = a$olduğundan, yüzey alan elemanı $ds_r = a^2 \sin \theta \, d\theta \, d\phi$ şeklinde ifade edilir. Yük yoğunluğu $\sigma = 2r$ olduğundan ve $r = a$olduğu için $\sigma = 2a$ olur.
>**Adımlar:**
>1. **İntegralin Kurulumu:**
  $$
   Q = \int \sigma \, ds_r = \int_{0}^{2\pi} \int_{0}^{\pi} 2a \cdot a^2 \sin \theta \, d\theta \, d\phi
  $$
   Burada$ds_r = a^2 \sin \theta \, d\theta \, d\phi$olduğu için$2a \cdot a^2 = 2a^3$yazılır.
>2. **İntegralin Hesaplanması:**
   $$
    Q = 2a^3 \int_{0}^{2\pi} d\phi \int_{0}^{\pi} \sin \theta \, d\theta = 2a^3 \cdot 2\pi \cdot 2 = 8\pi a^3
   $$
>**Sonuç:**
Toplam yük miktarı $\boxed{8\pi a^3} \, \text{C}$ olarak bulunur.

### Hacimsel Yük Dağılımlarının İhtiva ettiği Toplam Yük Değeri

Hacimsel yük dağılımı, bir hacim içinde tanımlanmış bir yük yoğunluğu ile ifade edilir. Bu durumda, bu hacimsel yük dağılımı üzerinde bir diferansiyel yük miktarı aşağıdaki gibi ifade edilir:

$$dq = \rho \, dv$$

Burada $dv$ hacimsel yük dağılımının birim hacmini temsil eder. Bu durumda, bu hacimsel yük dağılımının ihtiva ettiği toplam yük miktarı aşağıdaki gibi hesaplanır:

$$Q = \int dq = \int \rho \, dv$$

Bu integrali çözmek için, $dv$ ifadesini, çalışılan koordinat sistemine uygun bir şekilde ifade etmek gerekmektedir.

>**Uygulama 8:** Yarıçapı $a$, yüksekliği $L$ olan bir silindirin içinde tanımlanmış bir hacimsel yük yoğunluğu $\rho_v = 3\rho^2\, \text{(C/m}^3)$ olan bir hacimsel yük dağılımı düşünelim. Silindir içindeki toplam yük miktarını hesaplayınız.
>**Çözüm:**
>Toplam yük miktarını hesaplamak için, hacimsel yük yoğunluğunu silindirin içinde integral almalıyız. Silindirin yarıçapı $\rho = a$olduğundan, hacim elemanı$dv = a \, d\rho \, d\phi \, dz$ şeklinde ifade edilir. Yük yoğunluğu $\rho_v = 3\rho^2$ olduğundan ve $\rho = a$ olduğu için $\rho_v = 3a^2$ olur.

>**Adımlar:**
>1. **İntegralin Kurulumu:**
  $$
   Q = \int \rho_v \, dv = \int_{0}^{2\pi} \int_{0}^{L} \int_{0}^{a} 3a^2 \cdot a \, d\rho \, dz \, d\phi
  $$
   Burada $dv = a \, d\rho \, dz \, d\phi$ olduğu için $3a^2 \cdot a = 3a^3$ yazılır.
>2. **İntegralin Hesaplanması:**  
  $$
   Q = 3a^3 \int_{0}^{2\pi} d\phi \int_{0}^{L} dz \int_{0}^{a} d\rho = 3a^3 \cdot 2\pi \cdot L \cdot a = 6\pi a^4 L
  $$

>**Uygulama 9:** Yarıçapı $a$ olan bir kürenin içinde tanımlanmış bir hacimsel yük yoğunluğu $\rho_v = 2r\, \text{(C/m}^3)$ olan bir hacimsel yük dağılımı düşünelim. Küre içindeki toplam yük miktarını hesaplayınız.
>**Çözüm:**
>Toplam yük miktarını hesaplamak için, hacimsel yük yoğunluğunu kürenin içinde integral almalıyız. Kürenin yarıçapı $r = a$ olduğundan, hacim elemanı $dv = a^2 \sin \theta \, d\theta \, d\phi \, dr$ şeklinde ifade edilir. Yük yoğunluğu $\rho_v = 2r$ olduğundan ve $r = a$ olduğu için $\rho_v = 2a$ olur.
>**Adımlar:**
>1. **İntegralin Kurulumu:**
  $$
   Q = \int \rho_v \, dv = \int_{0}^{2\pi} \int_{0}^{\pi} \int_{0}^{a} 2a \cdot a^2 \sin \theta \, d\theta \, d\phi \, dr
  $$
   Burada $dv = a^2 \sin \theta \, d\theta \, d\phi \, dr$ olduğu için$2a \cdot a^2 = 2a^3$ yazılır.
>2. **İntegralin Hesaplanması:**
   $$
    Q = 2a^3 \int_{0}^{2\pi} d\phi \int_{0}^{\pi} \sin \theta \, d\theta \int_{0}^{a} dr = 2a^3 \cdot 2\pi \cdot 2 \cdot a = 8\pi a^4
   $$
>**Sonuç:**
Toplam yük miktarı $\boxed{8\pi a^4} \, \text{C}$ olarak bulunur.





