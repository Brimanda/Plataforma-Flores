$(document).ready(function () {
	$("#formulario_reg").validate(
		{
			rules: {
				regis_nombre: {
					required: true,
					minlength: 4
				},
				regis_usuario: {
					required: true,
				},
				regis_correo: {
					required: true,
					email: true
				},
				regis_contra: {
					required: true,
					minlength: 8
					
				},
				regis_confirma: {
					equalTo: "#regis_contra"
				},
				regis_numero: {
					required: true,
					number: true,
					maxlenght: 9
				},
				login_correo: {
					required: true,
					email: true
				},
				login_contra: {
					required: true,
					minlength: 8
				}

			},
			messages: {
				regis_nombre: {
					required: "Porfavor ingrese el nombre",
					minlength: "Porfavor ingresa un nombre válido"
				},
				regis_usuario: {
					required: "Porfavor ingrese un usuario"
				},
				regis_correo: {
					required: "Porfavor ingrese el correo",
					email: "El correo debe contener un formato válido"
				},
				regis_contra: {
					required: "Porfavor ingrese una contraseña"
				},
				regis_confirma: {
					equalTo: "Las contraseñas no coinciden"
				},
				login_correo: {
					required: "Porfavor ingrese el correo",
					email: "El correo debe contener un formato válido"
				},
				login_contra: {
					required: "Porfavor ingrese una contraseña válida"
				}
			}
		}
	);
});