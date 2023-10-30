<template>

</template>

<script>
const { $pdfMake } = useNuxtApp();

function printPdf(action) {
    const docDefinition = {
        content: [
        {text: 'Rechung', style: 'header'},
		{
			style: 'tableExample',
			table: {
        widths: ['auto', 300, 'auto', 'auto'],
				body: [
					['Anzahl', 'Bezeichnung', 'Einzelpreis', 'Gesamt'],
					['2', 'Entwicklung Backend (Strapi CMS)', '100€', '200€']
				]
			}
		},
        ],
        styles: {
		header: {
			fontSize: 18,
			bold: true,
			margin: [0, 0, 0, 10]
		},
		tableExample: {
			margin: [0, 5, 0, 0]
		},
	},
    };
    
    if (action === 2) {
        const pdf = createPdf(docDefinition);
        pdf.download('PPRA.pdf');
    }
}
</script>