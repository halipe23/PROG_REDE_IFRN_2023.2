import struct

def ler_cabecalho_arquivo(tcpdump):
    cabecalho = tcpdump.read(24)
    magic_number, major_version, minor_version, reserved1, reserved2, snaplen, fcs_linktype = struct.unpack('IHHIIII', cabecalho)

    print(f"Número Mágico: {magic_number}")
    print(f"Versão Principal: {major_version}")
    print(f"Versão Secundária: {minor_version}")
    print(f"Reservado1: {reserved1}")
    print(f"Reservado2: {reserved2}")
    print(f"SnapLen: {snaplen}")
    print(f"FCS e Tipo de Link: {fcs_linktype}")

def ler_pacote(tcpdump):
    timestamp_seconds, timestamp_microseconds, captured_length, original_length = struct.unpack('IIII', tcpdump.read(16))

    print(f"Timestamp (Segundos): {timestamp_seconds}")
    print(f"Timestamp (Microssegundos): {timestamp_microseconds}")
    print(f"Comprimento Capturado do Pacote: {captured_length}")
    print(f"Comprimento Original do Pacote: {original_length}")
    
    pacote_data = tcpdump.read(captured_length)
    print(f"Dados do Pacote: {pacote_data}")