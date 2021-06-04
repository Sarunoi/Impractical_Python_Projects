""" Hide a message in a docx document using a white font."""
import docx
from docx.shared import RGBColor, Pt
import operator

rgb_colors_sets = {
    "red": {
        'r': 255,
        'g': 0,
        'b': 0
    },
    "green": {
        'r': 0,
        'g': 255,
        'b': 0
    },
    "blue": {
        'r': 0,
        'g': 0,
        'b': 255
    },
}


def get_paragraphs_list(file):
    document = docx.Document(file)
    return [paragraph.text for paragraph in document.paragraphs]


def validate_fake_msg(fake_paragraphs, real_paragraphs):
    empty_paragraphs_in_fake_msg = fake_paragraphs.count("")
    len_real_msg = len(real_paragraphs)
    if operator.le(empty_paragraphs_in_fake_msg, len_real_msg):
        raise ValueError(
            "Fake msg does not have enough empty paragraphs to cover"
            f"real msg. We need {len_real_msg -  empty_paragraphs_in_fake_msg}"
            " more empty lines in fake msg to be able to cover real msg.")


def get_template_doc_with_letterhead(template_file):
    # load template that sets style, font, margins, etc.
    template_doc = docx.Document(template_file)

    # add letterhead:
    template_doc.add_heading('Morland Holmes', 0)
    subtitle = template_doc.add_heading('Global Consultanting & Negotiations', 1)
    subtitle.alignment = 1
    template_doc.add_heading('', 1)
    template_doc.add_paragraph('December 17, 2015')
    template_doc.add_paragraph('')
    return template_doc


def set_spacing(paragraph):
    """Use docx to set line spacing between paragraphs."""
    paragraph_format = paragraph.paragraph_format
    paragraph_format.space_before = Pt(0)
    paragraph_format.space_after = Pt(0)


def fill_doc_with_real_msg_covering_fake_msg(doc, fake_list, real_list):
    for line in fake_list:
        if real_list and line == '':
            paragraph = doc.add_paragraph(real_list.pop(0))
            paragraph_index = len(doc.paragraphs) - 1

            run = doc.paragraphs[paragraph_index].runs[0]
            run.font.color.rgb = RGBColor(
                **rgb_colors_sets["red"])  # make it red to test

        else:
            paragraph = doc.add_paragraph(line)

        set_spacing(paragraph)
    # TODO: Should this method return doc? It's not necessary, but it
    #  would be in functional programming mindset.


def main():
    fake_list = get_paragraphs_list('fakeMessage.docx')

    real_list = [
        paragraph if paragraph != '' else None
        for paragraph in get_paragraphs_list('realMessage_Vig.docx')
    ]

    # TODO: what is a good way to filter out empty strings? I could do filter,
    #  list comprehension, loop, anything else? Which is best?
    # real_list = list(filter(lambda x: x != '', real_list_with_empty_strs))

    validate_fake_msg(fake_list, real_list)

    doc = get_template_doc_with_letterhead('template.docx')

    fill_doc_with_real_msg_covering_fake_msg(doc, fake_list, real_list)

    doc.save('ciphertext_message_letterhead.docx')

    print("Done")


if __name__ == '__main__':
    main()
