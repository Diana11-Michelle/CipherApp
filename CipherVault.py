from kivymd.app import MDApp
from kivy.lang import Builder
from plyer import filechooser
from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog
from kivy.app import App
from kivymd.uix.textfield import MDTextField
import random
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from Crypto.Hash import SHA3_256
from Crypto.Hash import HMAC



KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True

MDScreen:

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            #1st screen

            MDScreen:
                name: "scr 1" 
                id:scr1


                MDTopAppBar:
                    title: "Cipher Vault"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]
                MDLabel:
                    text: "Screen 1"
                    halign: "center"
                MDFloatLayout:

                    MDRoundFlatIconButton:
                        text:"Choose File(Original)"
                        icon:"file"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.7}
                        on_release: app.open_file_chooser()
                    MDRoundFlatIconButton:
                        text:"Choose File(Modified)"
                        icon:"file"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .7, "center_y":.6}
                        on_release: app.open_file_chooser2()

                    MDRoundFlatButton:
                        text:"Enter Keys"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .2, "center_y":.4}
                        on_release: app.trigger_extract_file_keys()                   

                    MDTextField:
                        id: clear_secret_message_label
                        multiline: True
                        hint_text: "Secret message "
                        halign: "left"
                        pos_hint: {"center_x": .6, "center_y": .3}
                        theme_text_color: "Hint"
                        line_color_focus: "#e7e4c0"
                        icon_left: "email"
                        text_color: app.theme_cls.primary_color                   

                    MDRectangleFlatButton:
                        text:"Next"                         
                        text_color: "#4a4939"
                        md_bg_color: "#2ecc71"
                        pos_hint:{"center_x": .8, "center_y":.1} 
                        on_release:root.ids.screen_manager.current = "scr 4"  
                    MDRectangleFlatButton:
                        text:"Finish"                        
                        text_color: "#FFFFFF"
                        md_bg_color: "#FF0000"
                        pos_hint:{"center_x": .6, "center_y":.1}
                        on_press: app.close_window() 
                        #on_press:app.clear_inputs_and_outputs()     
                    MDRectangleFlatButton:
                        text:"Clear"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .8, "center_y":.4} 
                        on_press:app.clear_inputs_and_outputs() 
                    MDRectangleFlatButton:
                        text:"View Message"
                        md_bg_color: "#e7e4c0"
                        text_color: "#4a4939"
                        pos_hint:{"center_x": .8, "center_y":.2} 
                        on_release : app.trigger_get_files()

            #4th screen
            MDScreen:
                name: "scr 4"

                MDTopAppBar:
                    title: "Ciper Vault"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items:
                        [['menu', lambda x: nav_drawer.set_state("open")]]

                MDLabel:
                    text: "Screen 4"
                    halign: "center"
                MDLabel:
                    id:opened_file
                    text: " Write Secret Message"
                    theme_text_color: "Primary"
                    pos_hint:{"center_x": .5, "center_y":.8}
                MDTextField:
                    id: txt
                    multiline: True
                    hint_text: "Enter a replacement word"
                    helper_text: "This will be used to modify a random paragraph"
                    helper_text_mode: "on_focus"
                    halign: "left"
                    pos_hint: {"center_x": .5, "center_y": .7}
                    theme_text_color: "Hint"
                    line_color_focus: "#e7e4c0"
                    icon_left: "email"
                    text_color: app.theme_cls.primary_color

                MDRoundFlatButton:
                    text:"Replace Word"  #[generate paragraph,replace the word]
                    md_bg_color: "#e7e4c0"
                    text_color: "#4a4939"
                    pos_hint: {"center_x": .2, "center_y": .5}  # Position of the button
                    on_release: app.replace_word() 

                MDRoundFlatButton:
                    text:"Save Message" #'saves the file too' [save file]
                    md_bg_color: "#e7e4c0"
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .2, "center_y":.4}
                    on_release:app.show_hmac_key_input_popup()

                MDRectangleFlatButton:
                    text:"Clear"
                    md_bg_color: "#e7e4c0"
                    text_color: "#4a4939"
                    pos_hint:{"center_x": .2, "center_y":.2} 
                    on_press:app.clear_inputs2_and_outputs()   

                MDRectangleFlatButton:
                    text:"Finish"                   
                    text_color: "#4a4939"
                    md_bg_color: "#2ecc71"
                    pos_hint:{"center_x": .8, "center_y":.1} 
                    on_press: app.close_window()
                MDRectangleFlatButton:
                    text:"Back"                   
                    text_color: "#4a4939"
                    md_bg_color: "#3498db"
                    pos_hint:{"center_x": .6, "center_y":.1} 
                    on_release:root.ids.screen_manager.current = "scr 1"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            type:"standard"
            close_on_click:True


            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Cryptosteg"
                    title_color: "#e7e4c0"
                    source: "logo1.png"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"
                    #title_font_style:""
                    #title_font_size:""

                MDNavigationDrawerLabel:
                    text: "Select Action" 
                    text_halign:"center"

                MDNavigationDrawerDivider:   

                MDNavigationDrawerLabel:
                    text: "Extract"

                DrawerClickableItem:
                    icon: "message-reply-text"
                    text: "Extract message"
                    on_release:
                        root.ids.screen_manager.current = "scr 1"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Hide"


                DrawerClickableItem:
                    icon: "message-draw"
                    text: "Embed message"
                    on_release:
                        root.ids.screen_manager.current = "scr 4"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Rate App"

                DrawerLabelItem:
                    icon: "account-settings"
                    text: "Settings"
                DrawerLabelItem:
                    icon: "help-circle"
                    text: "Help & Feedback"


'''


class Example(MDApp):
    dialog = None  # the dialog attribute
    selected_file = None  # selected_file attribute/before
    dialog2 = None  # Initialize dialog2 to None
    selected_file2 = None  # This attribute stores the second file/before
    filename = None
    hmac_key = None
    selected_file3 = None  # selected_file attribute/after
    selected_file4 = None  # selected_file attribute/after
    selected_file6 = None  #
    selected_file5 = ''

    list1 = ['boy', 'girl', 'cherry', 'date', 'house', 'tree', 'plane', 'shoe', 'dog', 'cat']
    list2 = ['he', 'she', 'you', 'me', 'I', 'we', 'us', 'this', 'them', 'that']
    list3 = ['run', 'jump', 'write', 'sing', 'dance', 'eat', 'study', 'create', 'build', 'think']
    list4 = ['now', 'today', 'yesterday', 'soon', 'later', 'always', 'often', 'rarely', 'never']
    list5 = ['small', 'large', 'tiny', 'massive', 'gigantic', 'miniature', 'colossal']
    random_paragraph = None
    modified_paragraph = None

    def build(self):
        self.theme_cls.theme_style = "Dark"  # name of the color scheme in use"Purple", "Red""Teal"

        return Builder.load_string(KV)

    # This is for screen 1
    # file choooser of the original file starts here

    def open_file_chooser(self):

        filechooser.open_file(on_selection=self.on_file_selected)

    def on_file_selected(self, selection):
        print(selection)
        if selection:
            self.selected_file = selection[0]  # Store the selected file
            self.show(self.selected_file)  # Display selected file
            self.on_text_file_selected(self.selected_file)  # Process selected file
            self.extract_file_keys(self.selected_file)  # Extract keys
            self.selected_original_file(self.selected_file)  # pass it to that method

    def on_text_file_selected(self, selected_file):  # Add selected_file as a parameter
        self.selected_file = selected_file  # stores the selected file
        print('The selected Original File:', selected_file)  # print the selected file
        print('The selected', selected_file)

    def show(self, selected_file):
        self.selected_file = selected_file  # Store the selected file
        if not self.dialog:
            scrollView = ScrollView(size_hint_y=None, height="300dp")

            # MDTextField for editable text
            text_input = MDTextField(
                multiline=True,
                hint_text="Original File Content",
                write_tab=False
            )
            try:
                with open(self.selected_file, "r", encoding="utf-8", errors="ignore") as file:
                    file_content = file.read()
                    text_input.text = file_content
                    # opens the file contents on screen 2 as wells

            except Exception as e:
                text_input.text = f"Error reading file: {str(e)}"

            scrollView.add_widget(text_input)

            submit_button = MDRaisedButton(
                text="Submit",
                on_release=self.submit_text
            )

            self.dialog = MDDialog(
                title="Opened File",
                type="custom",
                content_cls=scrollView,
                buttons=[submit_button]
            )

        self.dialog.auto_dismiss = True
        self.dialog.open()

    def submit_text(self, instance):
        text_input = self.dialog.content_cls.children[0]
        text = text_input.text
        if text:
            # Show a popup to confirm that the text has been submitted
            self.confirm_dialog = MDDialog(
                title="Success",
                text="The Original text has been submitted successfully.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.close_dialog
                    )
                ]
            )
            self.confirm_dialog.open()

    def close_dialog(self, instance):
        self.dialog.dismiss()
        self.confirm_dialog.dismiss()

    # file chooser of the original file ends here
    # file chooser of the modified file begins here
    def open_file_chooser2(self):

        filechooser.open_file(on_selection=self.on_file_selected2)

    def on_file_selected2(self, selection2):
        print(selection2)
        if selection2:
            self.selected_file2 = selection2[0]  # Store the selected file
            self.on_text_file_selected2(self.selected_file2)  # Process selected file
            self.show2(self.selected_file2)  # Display selected file
            self.select_modified_file(self.selected_file2)  # pass it to that method

    def on_text_file_selected2(self, selected_file2):  # Add selected_file as a parameter
        print('The selected modified file: ', selected_file2)  # print the selected file
        print('The selected modified', selected_file2)

    def show2(self, selected_file2):
        self.selected_file = selected_file2  # stores the selected second file
        if not self.dialog2:
            scrollView2 = ScrollView(size_hint_y=None, height="300dp")

            # MDTextField for editable text
            text_input2 = MDTextField(
                multiline=True,
                hint_text="Modified File Content",
                write_tab=False
            )
            try:
                with open(selected_file2, "r", encoding="utf-8", errors="ignore") as file:
                    file_content = file.read()
                    text_input2.text = file_content
                    # opens the file contents on screen 2 as wells

            except Exception as e:
                text_input2.text = f"Error reading file: {str(e)}"

            scrollView2.add_widget(text_input2)

            submit_button2 = MDRaisedButton(
                text="Submit",
                on_release=self.submit_text2
            )

            self.dialog2 = MDDialog(
                title="Opened File",
                type="custom",
                content_cls=scrollView2,
                buttons=[submit_button2]
            )
            self.dialog2.auto_dismiss = True
        self.dialog2.open()

    def submit_text2(self, instance):
        text_input3 = self.dialog2.content_cls.children[0]
        text = text_input3.text
        if text:
            # Show a popup to confirm that the text has been submitted
            self.confirm_dialog2 = MDDialog(
                title="Success",
                text="The Modified file content has been submitted successfully.",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: self.close_dialog2()
                    )
                ]
            )
            self.confirm_dialog2.open()

    def trigger_get_files(self):
        # self.selected_original_file(self.selected_file5)
        # self.select_modified_file(self.selected_file2)
        if not self.selected_file5 or not self.selected_file2:
            self.show_dialog("Please select the two files")
            return
        # Check if only one file is selected
        if not self.selected_file5 or not self.selected_file2:
            self.show_dialog("Please select the second file")
            return
        # Print both selected files
        print('Original File:', self.selected_file5)
        print('Modified File:', self.selected_file2)
        try:
            with open(self.selected_file5, 'r') as file:
                file_contents = file.read().encode('utf-8')
                # Separate the HMAC value from the file content
                file_lines = file_contents.split(b'\n')  # Splits the file content into lines
                # Extract the paragraph
                paragraph1 = file_lines[0]  # Extract the paragraph  in the first line)
                print('The original paragraph:', paragraph1)
            with open(self.selected_file2, 'r') as file:
                file_contents1 = file.read().encode('utf-8')
                # Separate the HMAC value from the file content
                file_lines = file_contents1.split(b'\n')  # Splits the file content into lines
                # Extract the paragraph
                paragraph2 = file_lines[0]  # Extract the paragraph  in the first line)
                print('The modified paragraph:', paragraph2)
            # Call compare_paragraphs with the extracted paragraphs
            self.compare_paragraphs(paragraph1, paragraph2)
        except FileNotFoundError as e:
            self.show_dialog(f"File not found: {e.filename}")

    def compare_paragraphs(self, paragraph1, paragraph2):
        # Split the paragraphs into lists of words
        words1 = paragraph1.lower().split()
        words2 = paragraph2.lower().split()

        # Find the unique words in each paragraph
        unique_words1 = set(words1) - set(words2)
        unique_words2 = set(words2) - set(words1)
        # Print the results
        print("Unique words in Paragraph 1:", unique_words1)
        print("Unique words in Paragraph 2:", unique_words2)
        # Convert unique_words2 to a list of strings if they are not already
        unique_words2_str = [word.decode('utf-8') if isinstance(word, bytes) else word for word in unique_words2]
        # Update the MDTextField with unique words from paragraph 2
        secret_message_field = self.root.ids.clear_secret_message_label
        secret_message_field.text = " ".join(unique_words2_str)

    def selected_original_file(self, selected_file1):
        self.selected_file5 = selected_file1
        if hasattr(self, 'selected_file'):
            print("Extracting paragraph 1 from:", self.selected_file5)
        else:
            print("No file selected!")

    def select_modified_file(self, selected_file2):
        if hasattr(self, 'selected_file'):
            print("Extracting paragraph 2 from:", self.selected_file2)
        else:
            print("No file selected!")

    def show_dialog(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

    # def press_extract(self, selected_file0, selected_file01):

    # def compare_paragraphs(self, selected_file6, selected_file5):

    def close_dialog2(self):
        self.dialog2.dismiss()
        self.confirm_dialog2.dismiss()

    # file chooser of the modified file ends here

    # the decrypting Algorithm begins here
    # Function to prompt the user to enter the file keys
    def extract_file_keys(self, selected_file):
        if hasattr(self, 'selected_file'):
            print("Extracting keys from:", self.selected_file)
        else:
            print("No file selected!")

    # Button click handler for triggering the extract_file_keys
    def trigger_extract_file_keys(self):
        if not self.selected_file:
            self.show_dialog5("Please Choose a file to enter a Key")
            return
        self.process_key()  # Call the process_key method

    def process_key(self):
        # Create text input for key entry
        user_key_input = MDTextField()

        # Define close button
        close_button = MDFlatButton(text="Cancel", on_release=self.close_dialog3)

        # Define submit button
        submit_button = MDFlatButton(text="Submit", on_release=lambda x: self.process_key_action(user_key_input.text))

        # Create dialog
        self.dialog = MDDialog(
            title="Enter Key",
            type="custom",
            content_cls=user_key_input,
            buttons=[close_button, submit_button]
        )

        # Open dialog
        self.dialog.open()

    # Method to close dialog3
    def close_dialog3(self, *args):
        self.dialog.dismiss()

    def close_dialog1_and_dialog3(self, *args):
        self.dialog.dismiss()
        self.dialog1.dismiss()

    def close_dialod2_and_dialog1(self, *args):
        self.dialog.dismiss()
        self.dialog2.dismiss()

    def show_dialog5(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

    # Method to process key action
    def process_key_action(self, user_key_input):
        try:
            # Convert user input to binary representation
            user_key_binary = ''.join(format(byte, '08b') for byte in user_key_input.encode())
            print("User Key Binary:", user_key_binary)

            # Open the file
            with open(self.selected_file, 'r') as file:
                file_content = file.read().encode('utf-8')

                # Separate the HMAC value from the file content
                file_lines = file_content.split(b'\n')  # Splits the file content into lines
                # Extract the stored HMAC, key, and paragraph
                stored_hmac = file_lines[2].split(b': ')[-1].strip()  # Extract the stored HMAC
                stored_hmac_hex = stored_hmac.decode('utf-8')  # Decode bytes to string
                stored_key = file_lines[3].split(b': ')[-1].strip()  # Extract the stored key
                paragraph = file_lines[0]  # Extract the paragraph  in the first line)

                # Convert stored key to binary representation
                stored_key_binary = stored_key.decode('utf-8')
                print("Stored Key Binary:", stored_key_binary)

                # Print the extracted values for verification
                print("Stored HMAC:", stored_hmac_hex)
                print("Stored Key:", stored_key)
                print("Paragraph:", paragraph)

                # Compare provided key with stored key
                if user_key_binary == stored_key_binary:
                    print("Key verification successful.")
                    with open(self.selected_file, 'rb') as files:
                        file_content = files.read()
                        # Extract the paragraph from the file content
                        file_lines = file_content.split(b'\n')  # Split the file content into lines
                        paragraph = file_lines[0].strip()  # Extract and strip the paragraph (removes whitespaces)
                        print("Paragraph of the original file:",
                              paragraph.decode('utf-8'))  # Decodes from bytes to string
                        calculated_hmac = HMAC.new(user_key_input.encode(), paragraph, digestmod=SHA3_256).hexdigest()
                        print("Calculated HMAC:", calculated_hmac)
                    # Compare the calculated HMAC with the stored HMAC
                    if calculated_hmac == stored_hmac_hex:
                        print("HMAC verification successful. The message is authentic.")
                    else:
                        print("HMAC verification failure! The message may have been tampered with.")
                    self.dialog1 = MDDialog(
                        title="Key Verification and HMAC Success!",
                        text="The message is Authentic. You can proceed to view the message.",
                        buttons=[
                            MDFlatButton(
                                text="CLOSE",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                                on_release=lambda x: self.close_dialog1_and_dialog3()
                            )
                        ]
                    )
                    self.dialog1.open()

                    with open(self.selected_file, 'rb') as files:
                        file_content = files.read()
                        # Extract the paragraph from the file content
                        file_lines = file_content.split(b'\n')  # Split the file content into lines
                        paragraph = file_lines[0].strip()  # Extract and strip the paragraph (removes whitespaces)
                        print("Paragraph of the original file:",
                              paragraph.decode('utf-8'))  # Decodes from bytes to string
                        calculated_hmac = HMAC.new(user_key_input.encode(), paragraph, digestmod=SHA3_256).hexdigest()
                        print("Calculated HMAC:", calculated_hmac)
                    # Compare the calculated HMAC with the stored HMAC
                    if calculated_hmac == stored_hmac_hex:
                        print("HMAC verification successful. The message is authentic.")
                    else:
                        print("HMAC verification failure! The message has tampered with.")
                        dialog4 = MDDialog(
                            title="HMAC Verification Failure!",
                            text=" File contents cannot be trusted.Message has been tampered with!",
                            buttons=[
                                MDFlatButton(
                                    text="CLOSE",
                                    theme_text_color="Custom",
                                    text_color=self.theme_cls.primary_color,
                                    on_release=lambda x: dialog4.dismiss()
                                )
                            ]
                        )
                        dialog4.open()

                else:
                    print("Key verification Failed")
                    self.dialog2 = MDDialog(
                        title="Key Verification Failure!",
                        text="Key verification Failed. File contents cannot be trusted.",
                        buttons=[
                            MDFlatButton(
                                text="CLOSE",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                                on_release=lambda x: self.close_dialod2_and_dialog1()
                            )
                        ]
                    )
                    self.dialog2.open()
        except Exception as e:
            print(f"Error occurred during key verification: {str(e)}")

        # the decrypting algorithm ends here

    # Screen1 ends here

    # Screen four begins from here

    # function to generate random paragraphs:
    def generate_sentence(self):
        noun = random.choice(self.list1)
        pronoun = random.choice(self.list2)
        verb = random.choice(self.list3)
        adverb = random.choice(self.list4)
        adjective = random.choice(self.list5)
        sentence = f"{pronoun} {verb} the {adjective} {noun} {adverb}."
        return sentence

    def generate_paragraph(self):
        paragraph = ""
        for _ in range(15):
            paragraph += self.generate_sentence() + " "
        return paragraph.strip()

    def modify_paragraph(self, paragraph, replacement_word):
        words = paragraph.split()
        word_to_replace = random.choice(words)
        modified_paragraph = paragraph.replace(word_to_replace, replacement_word, 1)
        return modified_paragraph

    def replace_word(self):
        user_input = self.root.ids.txt.text  # txt has the input of the user
        if not user_input:
            self.show_dialog6("Please enter a Secret Message")
            return
        self.random_paragraph = self.generate_paragraph()
        print("Random Paragraph:")
        print(self.random_paragraph)
        self.modified_paragraph = self.modify_paragraph(self.random_paragraph, user_input)
        print("\nModified Paragraph:")
        print(self.modified_paragraph)
        self.show_success_popup()

    def show_dialog6(self, message):
        dialog = MDDialog(
            text=message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                ),
            ],
        )
        dialog.open()

    # a method to show the popup where the user can enter the HMAC key
    def show_hmac_key_input_popup(self):
        # check if user input was entered
        user_input = self.root.ids.txt.text  # txt has the input of the user
        if not user_input:
            self.show_dialog6("Please enter a Secret Message")
            return
        # Create the text field for HMAC key input
        self.hmac_key_input = MDTextField(hint_text="Enter HMAC key")

        # Create the submit button
        submit_button = MDFlatButton(
            text="SUBMIT",
            on_release=self.on_hmac_key_submit
        )

        # Create and open the dialog
        self.hmac_key_dialog = MDDialog(
            title="HMAC Key",
            type="custom",
            content_cls=self.hmac_key_input,
            buttons=[submit_button]
        )
        self.hmac_key_dialog.open()
        # After the user inputs the HMAC key, submits it,perform HMAC calculation, save the files.

    def on_hmac_key_submit(self, instance):
        # Retrieve the key from the input/Create an HMAC object with the provided key and SHA3-256 algorithm
        hmac_key = self.hmac_key_input.text  # encodes the key string

        # Close the HMAC key input dialog
        self.hmac_key_dialog.dismiss()

        # Now proceed to calculate HMAC, save files, and show success message
        self.save_to_file_with_hmac(hmac_key)

    def save_to_file_with_hmac(self, hmac_key):
        try:
            original_filename = 'original_paragraph.txt'
            modified_filename = 'modified_paragraph.txt'

            # Save the paragraphs to their respective files
            with open(original_filename, 'w') as file:
                file.write(self.random_paragraph)
            print(f"Original paragraph saved to file: '{original_filename}'")

            with open(modified_filename, 'w') as file:
                file.write(self.modified_paragraph)
            print(f"Modified paragraph saved to file: '{modified_filename}'")

            # Calculate HMAC for original paragraph
            # Read the original file
            with open(original_filename, 'rb') as file:
                # Read the entire content of the file
                content = file.read()
                # Split the content into paragraphs (assuming paragraphs are separated by newline characters)
                paragraphs = content.split(b'\n')
                # Take only the first paragraph
                first_paragraph = paragraphs[
                    0].strip()  # Extract and strip the first paragraph (remove leading/trailing whitespaces)
                print("Content of the original file:", first_paragraph)
                # Calculate HMAC for the first paragraph
                hmac_value1 = HMAC.new(hmac_key.encode(), first_paragraph, digestmod=SHA3_256).hexdigest()
                print("Calculated HMAC for the first paragraph:", hmac_value1)

            # Calculate HMAC for modified paragraph
            with open(modified_filename, 'rb') as file:
                content = file.read()
                print("Content of the modified file:",
                      content.decode('utf-8'))  # decodes the content originally in bytes to strings
                hmac_value2 = HMAC.new(hmac_key.encode(), content, digestmod=SHA3_256).hexdigest()

            # Convert HMAC key to binary representation
            hmac_key_binary = ''.join(format(byte, '08b') for byte in hmac_key.encode())

            # Attach the HMAC value to the original paragraph
            with open(original_filename, 'a') as file:
                file.write(f"\n\nHMAC (SHA3-256): {hmac_value1}\nKey: {hmac_key_binary}")
                print(f"File {original_filename} has been HMAC-protected with the provided password.")

            # Attach the HMAC value to the modified paragraph
            with open(modified_filename, 'a') as file:
                file.write(f"\n\nHMAC (SHA3-256): {hmac_value2}\nKey: {hmac_key_binary}")
                print(f"File {modified_filename} has been HMAC-protected with the provided password.")

            # After saving files and appending HMAC
            self.display_success_popup()

        except Exception as e:
            print(f"Error saving file: {str(e)}")  # Handle the error

    # popup menu of replaced words
    def show_success_popup(self):
        dialog = MDDialog(
            title="Success!",
            text="Words have been replaced successfully.",
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    # popup menu of saved paragraphs
    def display_success_popup(self):
        dialog = MDDialog(
            title="Success!",
            text="Paragraphs have been saved successfully with the HMAC.",
            buttons=[
                MDFlatButton(
                    text="CLOSE",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    # a method to close the window
    def close_window(self):
        App.get_running_app().stop()

    # Screen four ends here

    def clear_inputs_and_outputs(self):
        self.selected_file2 = ""
        self.selected_file5 = ''
        self.root.ids.clear_secret_message_label.text = ''
        self.selected_file6 = ''

    # to clear for screen4
    def clear_inputs2_and_outputs(self):
        self.root.ids.txt.text = ""
        self.random_paragraph = ""
        self.modified_paragraph = ""

    def clear_secret_message(self):
        self.root.ids.clear_secret_message_label.txt = ""

    # to clear choosen files
    def clear_chosen_files(self):
        self.selected_file = ""
        self.root.ids.text_input.text = ""
        self.root.ids.text_input2.text = ""
        self.root.ids.text_input3.text = ""
        self.selected_file2 = ""
        self.root.ids.user_key_input = ""

    # method that trigers the opened file


Example().run()

