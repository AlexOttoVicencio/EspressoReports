from weasyprint import HTML, CSS
import json
from data_loader import Data_Reader

def generate_report(data, output_file):
    html_template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        
    </head>
   <body>
    <!-- First Page (Title & Name) -->
    <div class="title-section">
        <div class="header">
            <img src="file:///C:/Users/Usuario/Desktop/Dev/EspressoReports/logos/logo_pucv.png" class="logo" alt="Logo 1" >
            <img src="file:///C:/Users/Usuario/Desktop/Dev/EspressoReports/logos/logo_ines.jpg" class="logo" alt="Logo 2">
        </div>
        <p>Tesis de postgrado con impacto <p>
        <div class="title">{data.get('nombre_proy', 'N/A')}</div>
        <span>
        <div class="subtitle">{data.get('nombre', 'N/A')}</div>
        <div class="subtitle">{data.get('correo', 'N/A')}</div>
        <div class="subtitle">Nro tel:{data.get('telefono', 'N/A')}</div>
        
 
    </div>

    
    <div class="content">
        <div class="section">
            <p><strong>Resumen</strong></p>
            <p> {data.get('resumen_proy', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>Objetivo general del proyecto</strong> </p>
            <p>{data.get('obj_general', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>Objetivos específicos del proyecto</strong> </p>
            <p>{data.get('obj_especificos', 'N/A')}</p>

        </div>
        <div class="section">
            <h2>Tesis de Postgrado</h2>
            <p><strong>Nombre del proyecto de postgrado</strong> (TESIS / INVESTIGACIÓN / OTRO)<strong></strong></p>
            <p> {data.get('nombre_tesis', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>Nombre del Programa: </strong>{data.get('nombre_programa', 'N/A')}</p>
            <p><strong>Fecha Inicio</strong> {data.get('fecha_inicio', 'N/A')}</p>
            <p><strong>Fecha Término</strong> (estimada) <strong>:</strong> {data.get('fecha_termino', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>Resumen:</strong> </p>
            <p> {data.get('resumen_tesis', 'N/A')}</p>
            <span></span>
            <span></span>
        </div>

        <div class="section">
            <h2>Problema</h2>
            <p><strong>¿Cuál es el problema,  oportunidad o necesidad que da origen a su proyecto?</strong></p>
            <p> {data.get('problema', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>¿A quienes afecta este problema, oportunidad o necesidad?</strong></p>
            <p> {data.get('afectados', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong> ¿Cuál es el tamaño del  problema, oportunidad o necesidad? </strong></p>
            <p> {data.get('tamano', 'N/A')}</p>
            <span></span>
            <span></span>
            
        </div>

        <div class="section">
            <h2>Solución</h2>
            <p><strong>¿En qué consiste su propuesta de solución? </strong></p>
            <p> {data.get('solucion', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>¿Cuál es el estado del arte?</strong></p>
            <p> {data.get('estado_arte', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>Grado de diferenciación de su propuesta.</strong></p>
            <p> {data.get('grado_diferenciacion', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>¿Cuál es la hipótesis que se pondrá a prueba?</strong></p>
            <p> {data.get('hipotesis', 'N/A')}</p>
            <span></span>
            <span></span>
        </div>

        <div class="section">
            <h2>Oportunidad de mercado</h2>
            <p><strong>¿Cuál es el mercado objetivo de su propuesta? </strong></p>
            <p> {data.get('mercado_obj', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>¿Cuál es su propuesta de continuidad?</strong></p>
            <p> {data.get('continuidad', 'N/A')}</p>
            <span></span>
            <span></span>
            <p><strong>8.4 Potencial vinculación con el entorno socioproductivo</strong></p>
            <p>{data.get('vinculacion_entorno', 'N/A')}</p>
            <span></span>
            <span></span>
        </div>
        <div class="section">
            <h2>Antecedentes del Director(a)</h2>
            <p><strong>Nombre:</strong>{data.get('nombre_dir', 'N/A')}</p>
            <p><strong>Rut:</strong>{data.get('rut_dir', 'N/A')}</p>
            <p><strong>Curriculum:</strong>{data.get('cv_dir', 'N/A')}</p>
        </div>
        <div class="section">
    <h2>Profesor (a) Guía PUCV </h2>
        <table>
            <tr>
                <th>Nombre</th>
                <th>Rut</th>
                <th>Unidad Académica</th>
            </tr>
            {professors_table_html}  
        </table>
    </div>

        <div class="section">
        <h2>Plan de trabajo y presupuesto (25%)</h2>
        
      <table>
        <tr>
            <th>Nro</th>
            <th>Actividad</th>
            <th>Descripción</th>
            <th>Presupuesto</th>
            <th>Mes/es ejecución</th>
        </tr>
        {plan_table_html}  
    </table>

        
        </div>
        
        <div class="section">
            <p><strong>El presupuesto total:</strong> {data.get('presupuesto_total', 'N/A')}</p>
        </div>

    </div>
    <!-- Page Break Here -->

    
</body>

    </html>
    '''
    HTML(string=html_template).write_pdf(output_file, stylesheets=["styles/tesis_post.css"])
    print(f"Report saved as {output_file}")
    

# Example data dictionary
data = {
    
}




#Generating object with the direction of the csv
report = Data_Reader("tesis_form_data.csv")

#this returns the direction
print(report.get_filename())

#I get the file
data_list = report.get_file()  # List of lists

#I get the column names
header = data_list[0]  # First row contains column names}
print(f"this is the header {header}")


def generate_plan_table(plan_presupuesto):
    rows = []
    activity_number = 1  # Counter for activity numbering
    
    for obj in plan_presupuesto:
        obj_especifico = obj["obj_especifico"]

        # Add a row for the objective itself (spanning columns)
        obj_html = f"""
        <tr>
            <td colspan="5"><strong>Obj. Específico: {obj_especifico}</strong></td>
        </tr>
        """
        rows.append(obj_html)

        for actividad in obj["actividades"]:
            nombre_act = actividad["nombre_act"]
            descripcion = actividad["descripcion"]
            presupuesto = actividad["presupuesto"]
            meses = actividad["meses"]

            # Create a row for each activity
            row_html = f"""
            <tr>
                <td>{activity_number}</td>
                <td>{nombre_act}</td>
                <td>{descripcion}</td>
                <td>{presupuesto}</td>
                <td>{meses}</td>
            </tr>
            """
            rows.append(row_html)
            activity_number += 1

    return "\n".join(rows)  # Convert list to a single string of HTML rows

def generate_professors_table(professors):
    rows = []
    
    for prof in professors:
        nombre = prof.get("nombre_guia", "N/A")
        rut = prof.get("rut_guia", "N/A")
        unidad_academica = prof.get("unidad_academica_guia", "N/A")

        row_html = f"""
        <tr>
            <td>{nombre}</td>
            <td>{rut}</td>
            <td>{unidad_academica}</td>
        </tr>
        """
        rows.append(row_html)

    return "\n".join(rows)



# Iterate over the data rows (excluding header) 
for index, row in enumerate(data_list[1:], start=1):
    data_dict = {header[i]: row[i] for i in range(len(header))}
    

    
    # Convert plan_presupuesto if it's a JSON string
    plan_presupuesto = json.loads(data_dict.get("plan_presupuesto", "[]"))
    profesor_guia = json.loads(data_dict.get("profesor_guia", "[]"))  # Parse guide professors

    nombre = data_dict.get("nombre", "unknown").replace(" ", "_")
    output_filename = f"thesis_reports/report_{index}_{nombre}.pdf"

    plan_table_html = generate_plan_table(plan_presupuesto)
    professors_table_html = generate_professors_table(profesor_guia)  # Generate guide professor table

    html_output = f'''
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
        <h1>Report for {data_dict.get("nombre", "N/A")}</h1>

        <h2>Plan de Presupuesto</h2>
        <table>
            <tr>
                <th>Nro</th>
                <th>Actividad</th>
                <th>Descripción</th>
                <th>Presupuesto</th>
                <th>Mes/es ejecución</th>
            </tr>
            {plan_table_html}  
        </table>

        <h2>Profesor (a) Guía PUCV</h2>
        <table>
            <tr>
                <th>Nombre</th>
                <th>Rut</th>
                <th>Unidad Académica</th>
            </tr>
            {professors_table_html}  
        </table>
    </body>
    </html>
    '''

    generate_report(data_dict, output_filename)
    