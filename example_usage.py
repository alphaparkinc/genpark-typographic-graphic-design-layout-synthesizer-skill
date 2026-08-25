from client import TypographicGraphicDesignLayoutSynthesizerClient

def main():
    client = TypographicGraphicDesignLayoutSynthesizerClient()
    res = client.synthesize_typographic_graphic_poster('NEURAL ARCHITECTURES', 'BAUHAUS_MINIMALIST_VECTOR', 300)
    print('Graphic Job: ' + res['graphic_job_id'] + ' (' + res['design_style'] + ')')
    print('Headline: "' + res['headline_rendered'] + '" | Kerning Accuracy: ' + str(res['lettering_kerning_accuracy_pct']) + '%')
    print('Poster URL: ' + res['rendered_print_ready_url'] + ' (SVG Outlines: ' + str(res['svg_text_outlines_exported']) + ')')

if __name__ == '__main__':
    main()
