from flask import(
	Blueprint,render_template,request,redirect,url_for,current_app
)
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
bp=Blueprint('portfolio',__name__,url_prefix='/')

@bp.route('/',methods=['GET'])
def index():
	return render_template('portfolio/index.html')

@bp.route('/mail',methods=['POST'])
def mail():
	name=request.form.get('name')
	email=request.form.get('email')
	message=request.form.get('message')
	if request.method=='POST':
		print(email,name,message)
		#send_email(email,name,message)

		#sent(email,"Nuevo contacto",message)
		sent(email,name,message)
		sent_cliente(email,name,message)
		#return render_template('portfolio/sent_mail-section.html')
	return render_template('portfolio/sent_mail.html');




def sent(email,name,message):

	#sg=sendgrid.SendGridAPIClient(api_key=current_app.config['SENGRID_KEY'])
	sg = SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
	from_email=Email(current_app.config['FROM_EMAIL'])
	#to_email=To('reyson_es@hotmail.es')
	to_email=To('reyson_es@hotmail.es',substitutions={
		"-name-":name,
		"-email-":email,
		"-message-":message
		})
	html_content="""
<h1 style="color: #5e9ca0;">Hola Reyson, <span style="color: #2b2301;">&nbsp;-name-</span> quiere ponerse en contacto contigo!</h1>
<h2 style="color: #2e6c80;">-name- ha dejado este mensaje:</h2>
<p><em>-message-</em></p>
<h2 style="color: #2e6c80;">Sus datos son:</h2>
<ol style="list-style: none; font-size: 14px; line-height: 32px; font-weight: bold;">
<li style="clear: both;"><img style="float: left;" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimg.icons8.com%2Fplasticine%2F2x%2Fname.png&amp;f=1&amp;nofb=1" alt="interactive connection" width="45" /> Nombre: -name-</li>
<li style="clear: both;"><img style="float: left;" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmaxcdn.icons8.com%2FShare%2Ficon%2Fnolan%2FUser_Interface%2Femail1600.png&amp;f=1&amp;nofb=1" alt="html cleaner" width="45" /> Correo: -email-</li>
</ol>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p><strong>Ponte en contacto lo mas pronto posible!</strong></p>
	"""
	#content=Content('text/plain',content)
	#mail=Mail(from_email,to_email,"Nuevo contacto",content)
	mail=Mail(from_email,to_email,"Nuevo contacto",html_content=html_content)
	response=sg.client.mail.send.post(request_body=mail.get())
	print(response)

def sent_cliente(email,name,message):

	#sg=sendgrid.SendGridAPIClient(api_key=current_app.config['SENGRID_KEY'])
	sg = SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
	from_email=Email(current_app.config['FROM_EMAIL'])
	#to_email=To('reyson_es@hotmail.es')
	to_email=To(email,substitutions={
		"-name-":name,
		"-email-":email,
		"-message-":message
		})
	html_content="""
	<p>nombre: -name- </p>
	<p>correo: -email- </p>
	<p>mensaje: -message- </p>
	"""
	#content=Content('text/plain',content)
	#mail=Mail(from_email,to_email,"Nuevo contacto",content)
	mail=Mail(from_email,to_email,"Nuevo contacto",html_content=html_content)
	response=sg.client.mail.send.post(request_body=mail.get())
	print(response)
