# SAE_ARN

VERSION IPYNB => <a href="https://github.com/m0tyr/SAE_ARN/blob/main/using_biology.ipynb">lien</a> </br>












VERSION HTML </br>
↓↓↓↓↓↓↓↓↓↓↓

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
 
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<div id="a023b3ed" class="cell markdown">
<h1 id="notebook-de-présentation-de-la-sae-s0102">Notebook de
présentation de la SAE S01.02</h1>
</div>
<div id="47840237" class="cell markdown">
<h2 id="binôme">Binôme</h2>
<ul>
<li>ZHANG Claude</li>
<li>TLEMSANI Sofiane</li>
</ul>
</div>
<div id="e2dbe7e8" class="cell code" data-execution_count="25">
<div class="sourceCode" id="cb1"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> json <span class="im">import</span> <span class="op">*</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> copy</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> biology <span class="im">as</span> b</span>
<span id="cb1-4"><a href="#cb1-4" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> test_biology <span class="im">as</span> test_b</span>
<span id="cb1-5"><a href="#cb1-5" aria-hidden="true" tabindex="-1"></a> </span></code></pre></div>
</div>
<div id="f771db82" class="cell markdown">
<p>### QUESTION 1 :</p>
<p><em>Définir la fonction est_base prenant en paramètre un caractère et
retournant True si ce caractère correspond à une base de l'ADN (est un
des caractères A, T, G, C), et False sinon.</em></p>
</div>
<div id="91e225f6" class="cell code" data-execution_count="26">
<div class="sourceCode" id="cb2"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>b.est_base(<span class="st">&quot;C&quot;</span>)</span></code></pre></div>
<div class="output execute_result" data-execution_count="26">
<pre><code>True</code></pre>
</div>
</div>
<div id="c73939d5" class="cell markdown">
<h3 id="question-2-">QUESTION 2 :</h3>
<p><em>Définir la fonction est_adn prenant en paramètre une chaîne de
caractères et retournant True si la chaîne correspond à un ADN (est
constituée uniquement des caractères A, T, G, C), et False
sinon.</em></p>
</div>
<div id="1ea6f9a8" class="cell code" data-execution_count="27">
<div class="sourceCode" id="cb4"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>b.est_adn(<span class="st">&quot;ATGTCAAA&quot;</span>)</span></code></pre></div>
<div class="output execute_result" data-execution_count="27">
<pre><code>True</code></pre>
</div>
</div>
<div id="3620ed5d" class="cell markdown">
<h3 id="question-3-">QUESTION 3 :</h3>
<p><em>Définir la fonction arn prenant en paramètre une séquence d'ADN
et retournant la séquence ARN associée.</em></p>
</div>
<div id="085ce733" class="cell code" data-execution_count="28">
<div class="sourceCode" id="cb6"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>b.arn(<span class="st">&quot;ATGACCT&quot;</span>)</span></code></pre></div>
<div class="output execute_result" data-execution_count="28">
<pre><code>&#39;AUGACCU&#39;</code></pre>
</div>
</div>
<div id="425ee1d4" class="cell markdown">
<h3 id="question-4-">QUESTION 4 :</h3>
<p><em>Définir la fonction arn_to_codons prenant en paramètre une chaîne
de caractères correspondant à de l'ARN et découpant cet ARN en codons.
La fonction doit retourner un tableau contenant la liste des codons. Par
exemple, l'appel de la fonction arn_to_codons avec l'ARN "CGUUAGGGG"
doit retourner le tableau ["CGU", "UAG", "GGG"].</em></p>
</div>
<div id="10758ac8" class="cell code" data-execution_count="29">
<div class="sourceCode" id="cb8"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a>b.arn_to_codons(<span class="st">&quot;CUCGG&quot;</span>)</span></code></pre></div>
<div class="output execute_result" data-execution_count="29">
<pre><code>[&#39;CUC&#39;]</code></pre>
</div>
</div>
<div id="0b7a3991" class="cell markdown">
<h3 id="question-5-">QUESTION 5 :</h3>
<h5
id="remarque--les-chemins-de-fichier-sont-les-notres-vous-devenez-les-changer-en-fonction-de-où-ce-trouve-votre-répertoire-data-avec-codons_aajson">Remarque
: Les chemins de fichier sont les notres vous devenez les changer en
fonction de où ce trouve votre répertoire data avec codons_aa.json</h5>
<h4 id="partie-1-">Partie 1 :</h4>
<p><em>Définir la fonction load_dico_codons_aa qui prend en paramètre un
fichier au format JSON et retourne la structure de données chargée en
mémoire à partir du JSON.</em></p>
</div>
<div id="550c43e0" class="cell code" data-execution_count="30">
<div class="sourceCode" id="cb10"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a>dictionnaire <span class="op">=</span> b.load_dico_codons_aa(<span class="vs">r&quot;C:\Users\sofkh\Documents\sae_s01.02-main\data/codons_aa.json&quot;</span>)</span>
<span id="cb10-2"><a href="#cb10-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(dictionnaire)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>{&#39;UUU&#39;: &#39;Phenylalanine&#39;, &#39;UUC&#39;: &#39;Phenylalanine&#39;, &#39;UUA&#39;: &#39;Leucine&#39;, &#39;UUG&#39;: &#39;Leucine&#39;, &#39;CUU&#39;: &#39;Leucine&#39;, &#39;CUC&#39;: &#39;Leucine&#39;, &#39;CUA&#39;: &#39;Leucine&#39;, &#39;CUG&#39;: &#39;Leucine&#39;, &#39;AUU&#39;: &#39;Isoleucine&#39;, &#39;AUC&#39;: &#39;Isoleucine&#39;, &#39;AUA&#39;: &#39;Methionine&#39;, &#39;AUG&#39;: &#39;Methionine&#39;, &#39;GUU&#39;: &#39;Valine&#39;, &#39;GUC&#39;: &#39;Valine&#39;, &#39;GUA&#39;: &#39;Valine&#39;, &#39;GUG&#39;: &#39;Valine&#39;, &#39;UCU&#39;: &#39;Serine&#39;, &#39;UCC&#39;: &#39;Serine&#39;, &#39;UCA&#39;: &#39;Serine&#39;, &#39;UCG&#39;: &#39;Serine&#39;, &#39;CCU&#39;: &#39;Proline&#39;, &#39;CCC&#39;: &#39;Proline&#39;, &#39;CCA&#39;: &#39;Proline&#39;, &#39;CCG&#39;: &#39;Proline&#39;, &#39;ACU&#39;: &#39;Threonine&#39;, &#39;ACC&#39;: &#39;Threonine&#39;, &#39;ACA&#39;: &#39;Threonine&#39;, &#39;ACG&#39;: &#39;Threonine&#39;, &#39;GCU&#39;: &#39;Alanine&#39;, &#39;GCC&#39;: &#39;Alanine&#39;, &#39;GCA&#39;: &#39;Alanine&#39;, &#39;GCG&#39;: &#39;Alanine&#39;, &#39;UAU&#39;: &#39;Tyrosine&#39;, &#39;UAC&#39;: &#39;Tyrosine&#39;, &#39;CAU&#39;: &#39;Histidine&#39;, &#39;CAC&#39;: &#39;Histidine&#39;, &#39;CAA&#39;: &#39;Glutamine&#39;, &#39;CAG&#39;: &#39;Glutamine&#39;, &#39;AAU&#39;: &#39;Asparagine&#39;, &#39;AAC&#39;: &#39;Asparagine&#39;, &#39;AAA&#39;: &#39;Lysine&#39;, &#39;AAG&#39;: &#39;Lysine&#39;, &#39;GAU&#39;: &#39;Aspartic acid&#39;, &#39;GAC&#39;: &#39;Aspartic acid&#39;, &#39;GAA&#39;: &#39;Glutamic acid&#39;, &#39;GAG&#39;: &#39;Glutamic acid&#39;, &#39;UGU&#39;: &#39;Cysteine&#39;, &#39;UGC&#39;: &#39;Cysteine&#39;, &#39;UGA&#39;: &#39;Tryptophan&#39;, &#39;UGG&#39;: &#39;Tryptophan&#39;, &#39;CGU&#39;: &#39;Arginine&#39;, &#39;CGC&#39;: &#39;Arginine&#39;, &#39;CGA&#39;: &#39;Arginine&#39;, &#39;CGG&#39;: &#39;Arginine&#39;, &#39;AGU&#39;: &#39;Serine&#39;, &#39;AGC&#39;: &#39;Serine&#39;, &#39;GGU&#39;: &#39;Glycine&#39;, &#39;GGC&#39;: &#39;Glycine&#39;, &#39;GGA&#39;: &#39;Glycine&#39;, &#39;GGG&#39;: &#39;Glycine&#39;}
</code></pre>
</div>
</div>
<div id="4fdd4764" class="cell markdown">
<h4 id="partie-2-">Partie 2 :</h4>
<p><em>Définir la fonction codons_stop prenant en paramètre un
dictionnaire dont les clés sont les codons et les valeurs les acides
aminés correspondants (chaînes de caractères). La fonction retournera un
tableau contenant l'ensemble des codons stop, c'est-à-dire l'ensemble
des codons possibles avec les caractères AUGC qui ne sont pas des clés
du dictionnaire.</em></p>
</div>
<div id="409f955a" class="cell code" data-execution_count="31">
<div class="sourceCode" id="cb12"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a>b.codons_stop(dictionnaire)</span></code></pre></div>
<div class="output execute_result" data-execution_count="31">
<pre><code>[&#39;AGA&#39;, &#39;AGG&#39;, &#39;UAA&#39;, &#39;UAG&#39;]</code></pre>
</div>
</div>
<div id="f046c527" class="cell markdown">
<h3 id="question-6-">QUESTION 6 :</h3>
<p><em>Définir la fonction codons_to_aa prenant en paramètre un tableau
de codons (correspondant par exemple à une valeur retournée par la
fonction arn_to_codons) et le dictionnaire de correspondance entre
codons et acides aminés. La fonction devra retourner un tableau
contenant les acides aminés correspondant aux codons.</em></p>
</div>
<div id="2263bbb1" class="cell code" data-execution_count="24">
<div class="sourceCode" id="cb14"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a>b.codons_to_aa([<span class="st">&quot;CGU&quot;</span>, <span class="st">&quot;AAU&quot;</span>, <span class="st">&quot;UGA&quot;</span>, <span class="st">&quot;UAG&quot;</span>, <span class="st">&quot;CGU&quot;</span>],dictionnaire)</span></code></pre></div>
<div class="output execute_result" data-execution_count="24">
<pre><code>[&#39;Arginine&#39;, &#39;Asparagine&#39;, &#39;Tryptophan&#39;]</code></pre>
</div>
</div>
</body>
</html>
