import json
import os
from nbconvert import HTMLExporter
import nbformat

# Load JSON data
with open("course_content.json") as f:
    data = json.load(f)

# Initialize nbconvert HTML exporter
html_exporter = HTMLExporter()
html_exporter.template_name = 'full'  # or 'lab' for JupyterLab-style output

# Start building index.html
html = f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>{data['site_title']}</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <script>
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {{
            document.documentElement.classList.add('dark');
        }}
    </script>
    <!-- Tailwind CSS CDN -->
    <link href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css' rel='stylesheet'>
    <style>
        body {{
            background-color: #111827;
            color: #f9fafb;
        }}
        .prose {{
            color: #f9fafb;
        }}
        .prose h1, .prose h2, .prose h3 {{
            color: #60a5fa;
        }}
        pre code {{
            background-color: #1f2937;
            color: #f9fafb;
            display: block;
            padding: 1em;
            overflow-x: auto;
            border-radius: 0.5rem;
        }}
        code {{
            background-color: #374151;
            padding: 0.2em 0.4em;
            border-radius: 0.25rem;
        }}
        a {{
            color: #93c5fd;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        p {{
            margin-top: 1em;
            margin-bottom: 1em;
            line-height: 1.7;
        }}
    </style>
</head>
<body class='font-sans p-6'>
    <div class='max-w-3xl mx-auto'>
        <h1 class='text-4xl font-bold mb-2'>{data['site_title']}</h1>
        <p class='text-lg text-gray-300 mb-6'>{data['intro']}</p>

        <!-- Search Bar -->
        <input type="text" id="searchInput" placeholder="Ders ismiyle ara..." class="w-full p-2 mb-4 rounded bg-gray-800 text-white border border-gray-600">

        <h2 class='text-2xl font-semibold mb-4'>Dersler</h2>
        <div class='space-y-6' id="surahList">
"""

# Loop through posts and generate individual pages + list on index.html
for idx, post in enumerate(data["posts"]):
    ipynb_file = post["post"]
    html_file = ipynb_file.replace(".ipynb", ".html")
    tags_html = " ".join(
        f"<span class='inline-block bg-blue-200 text-blue-900 text-xs px-2 py-1 rounded mr-1'>{tag}</span>"
        for tag in post.get("tags", [])
    )

    # Read Jupyter notebook
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Convert to HTML
    post_html, _ = html_exporter.from_notebook_node(notebook_content)

    # Write individual surah page
    with open(html_file, "w", encoding='utf-8') as f_post:
        f_post.write(f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>{post['title']}</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link href='https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css' rel='stylesheet'>
    <style>
        body {{
            background-color: #aba8a7;
            color: #f9fafb;
        }}
        .prose {{
            color: #f9fafb;
        }}
        .prose h1, .prose h2, .prose h3 {{
            color: #60a5fa;
        }}
        pre code {{
            background-color: #1f2937;
            color: #f9fafb;
            display: block;
            padding: 1em;
            overflow-x: auto;
            border-radius: 0.5rem;
        }}
        code {{
            background-color: #374151;
            padding: 0.2em 0.4em;
            border-radius: 0.25rem;
        }}
        a {{
            color: #93c5fd;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        p {{
            margin-top: 1em;
            margin-bottom: 1em;
            line-height: 1.7;
        }}
    </style>
</head>
<body class='font-sans p-6'>
    <div class='max-w-3xl mx-auto'>
        <a href='../index.html' class='block mb-4'>← Eğitim Listesine Geri Dön</a>
        <h1 class='text-3xl font-bold mt-4'>{post['title']}</h1>
        <p class='text-sm text-gray-400 mb-4'>{post['date']}</p>
        {tags_html}
        <div class='prose max-w-none mt-4'>{post_html}</div>
    </div>
</body>
</html>
""")

    # Add Course card to index.html
    html += f"""
        <div class='border-b pb-4' id='surah-{idx}'>
            <h3 class='text-xl font-semibold surah-title'>{post['title']}</h3>
            <p class='text-sm text-gray-400'>{post['date']}</p>
            <p class='mb-2'>{post['summary']}</p>
            {tags_html}
            <a href='{html_file}' class='block mt-1'>Eğitime Git →</a>
        </div>
"""

# Close index.html and add search script
html += """
        </div>
    </div>

    <!-- Search Script -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const searchInput = document.getElementById('searchInput');
            const surahCards = document.querySelectorAll('#surahList .border-b');

            searchInput.addEventListener('input', function () {
                const query = this.value.toLowerCase();

                surahCards.forEach(card => {
                    const title = card.querySelector('.surah-title').textContent.toLowerCase();
                    if (title.includes(query)) {
                        card.style.display = '';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    </script>
</body>
</html>
"""

# Write final index.html
with open("index.html", "w", encoding='utf-8') as f:
    f.write(html)

print("✅ Courses generated with enhanced dark theme and working search! Open index.html to view it.")